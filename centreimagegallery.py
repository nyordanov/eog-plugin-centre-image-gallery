from gi.repository import GObject, Eog

class CentreImageGalleryPlugin(GObject.Object, Eog.WindowActivatable):
	window = GObject.property(type=Eog.Window)

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		thumb_view = self.window.get_thumb_view()

		self.selection_handler_id = thumb_view.connect( 'selection-changed', self.centre_thumb_view_cb, self )
		
		self.thumb_view_activate_handler_id = thumb_view.connect( 'draw', self.centre_thumb_view_cb, self )

	def do_deactivate(self):
		self.window.disconnect(self.selection_handler_id)

	@staticmethod
	def centre_thumb_view_cb(view, *args ):
		try:
			view.scroll_to_path( view.get_selected_items()[0], True, 0.5, 0.5 )
		except Exception:
			pass
