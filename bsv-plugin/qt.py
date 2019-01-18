from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import electroncash.version
from electroncash.i18n import _
from electroncash.plugins import BasePlugin, hook, Plugins
from electroncash import bitcoin
from electroncash.network import pick_random_server

class Plugin(BasePlugin):
    electrumcash_qt_gui = None
    # There's no real user-friendly way to enforce this.  So for now, we just calculate it, and ignore it.
    is_version_compatible = True

    def __init__(self, parent, config, name):
        BasePlugin.__init__(self, parent, config, name)

        self.wallet_windows = {}
        self.network=None

    def fullname(self):
        return 'BSV Plugin'

    def description(self):
        return _("Plugin that makes Electron Cash compatible with BSV chain. After it's enabled you can connect to the servers of BSV network.")

    def is_available(self):
        if self.is_version_compatible is None:
            version = float(electroncash.version.PACKAGE_VERSION)
            self.is_version_compatible = version >= MINIMUM_ELECTRON_CASH_VERSION
        return True


    def on_close(self):
        """
        BasePlugin callback called when the wallet is disabled among other things.
        """
        bitcoin.NetworkConstants.VERIFICATION_BLOCK_MERKLE_ROOT = "b8f9b1649d0bba75e2c2ea4be73395a0967397003f33a40653caca0ec6a73baa"
        bitcoin.NetworkConstants.VERIFICATION_BLOCK_HEIGHT = 560644
        self.network.checkpoint_height = 560644
        self.network.config.set_key("server_blacklist", [])
        self.network.blacklisted_servers = set(self.config.get('server_blacklist', []))
        self.network.auto_connect = True
        self.network.config.set_key("auto_connect", True)
        for s in self.network.recent_servers:
            self.network.recent_servers.remove(s)
        self.network.save_recent_servers()
        for window in list(self.wallet_windows.values()):
            self.close_wallet(window.wallet)

    @hook
    def update_contact(self, address, new_entry, old_entry):
        print("update_contact", address, new_entry, old_entry)

    @hook
    def delete_contacts(self, contact_entries):
        print("delete_contacts", contact_entries)

    @hook
    def init_qt(self, qt_gui):
        """
        Hook called when a plugin is loaded (or enabled).
        """
        self.electrumcash_qt_gui = qt_gui
        # We get this multiple times.  Only handle it once, if unhandled.
        if len(self.wallet_windows):
            return

        # These are per-wallet windows.
        for window in self.electrumcash_qt_gui.windows:
            self.load_wallet(window.wallet, window)

    @hook
    def load_wallet(self, wallet, window):
        """
        Hook called when a wallet is loaded and a window opened for it.
        """
        wallet_name = window.wallet.basename()
        self.network = window.network
        bitcoin.NetworkConstants.VERIFICATION_BLOCK_MERKLE_ROOT = "3848ff6c001ebf78ec1a798c2002f154ace4ba6c0f0a58ccb22f66934eda7143"
        bitcoin.NetworkConstants.VERIFICATION_BLOCK_HEIGHT = 540250
        self.network.checkpoint_height = 540250
        self.network.config.set_key("server_blacklist", [])
        self.network.blacklisted_servers = set(self.config.get('server_blacklist', []))
        # print(self.network.blockchain())
        self.wallet_windows[wallet_name] = window

    @hook
    def close_wallet(self, wallet):
        wallet_name = wallet.basename()
        window = self.wallet_windows[wallet_name]
        del self.wallet_windows[wallet_name]
