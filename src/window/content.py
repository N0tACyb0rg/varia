import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib, Gio

def window_create_content(self, threading):
    content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    self.total_download_speed_label = Gtk.Label(label=self.total_download_speed)

    header_button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)

    self.header_pause_content = Adw.ButtonContent()
    self.header_pause_content.set_icon_name("media-playback-pause-symbolic")
    self.header_pause_content.set_label(_("Pause All"))
    self.header_pause_button = Gtk.Button()
    self.header_pause_button.set_sensitive(False)
    self.header_pause_button.set_child(self.header_pause_content)
    self.header_pause_button.connect("clicked", lambda button: self.pause_all(self.header_pause_content))

    header_button_box.append(self.header_pause_button)

    header_expanding_box = Gtk.Box()
    Gtk.Widget.set_hexpand(header_expanding_box, True)
    header_expanding_box_1 = Gtk.Box()
    Gtk.Widget.set_hexpand(header_expanding_box_1, True)

    header_box.append(header_expanding_box)
    header_box.append(self.total_download_speed_label)
    header_box.append(header_expanding_box_1)
    header_box.append(header_button_box)

    header_bar = Adw.HeaderBar()
    header_bar.get_style_context().add_class('flat')
    header_bar.set_title_widget(header_box)
    content_box.append(header_bar)

    self.download_list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    self.download_list.set_margin_start(6)
    self.download_list.set_margin_end(6)
    self.download_list.set_margin_bottom(6)
    self.download_list.set_margin_top(6)

    scrolled_window = Gtk.ScrolledWindow()
    scrolled_window.set_child(self.download_list)
    scrolled_window.set_hexpand(True)
    scrolled_window.set_vexpand(True)

    content_box.append(scrolled_window)

    self.overlay_split_view.set_content(content_box)

    self.total_download_speed_calculator_thread = threading.Thread(target=self.total_download_speed_get, args=(self.downloads, self.total_download_speed_label))
    self.total_download_speed_calculator_thread.start()

    self.check_download_status_thread = threading.Thread(target=self.check_download_status)
    self.check_download_status_thread.start()
