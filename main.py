
import os
import sys


plugin_path = os.path.join(os.path.dirname(__file__), 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


from PyQt5.QtWidgets import QApplication
from network import Network
from cli_parser import CLIParser
from gui_main import MainWindow

def main():
    
    network = Network()
    cli = CLIParser(network)

    
    network.add_device("sensor")
    network.add_device("lamp")

    
    app = QApplication(sys.argv)
    window = MainWindow(network, cli)
    window.refresh()    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()