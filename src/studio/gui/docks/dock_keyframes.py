# === S Y N F I G ========================================================= */
#	file: docks/dock_keyframes.py
#	Description: Keyframes panel - tracks the Time, Length, Jump and Description
#                                  of an animation frame
#
#
#	Copyright (c) 2002-2005 Robert B. Quattlebaum Jr., Adrian Bentley
#   wxSynfig: Copyright (c) 2019 Austin Aigbe
#
#	This package is free software; you can redistribute it and/or
#	modify it under the terms of the GNU General Public License as
#	published by the Free Software Foundation; either version 2 of
#	the License, or (at your option) any later version.
#
#	This package is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#	General Public License for more details.


#include "docks/dockable.h"
import dockable
#include "docks/dock_canvasspecific.h"
from dock_canvasspecific import DockCanvasSpecific

#include <gtkmm/treeview.h>
#include "instance.h"
#include <gtkmm/actiongroup.h>
import wx


#namespace studio {

class KeyframeTreeStore;
class KeyframeTree;

class KeyframeActionManager;

# class: Dock_Keyframes
# Description: A Dockable dialog which holds the keyframe list

# class Dock_Keyframes : public Dock_CanvasSpecific
class DockKeyframes(DockCanvasSpecific):
	
{
	//The actions stuff
	Glib::RefPtr<Gtk::ActionGroup> action_group;

	/*
	void add_keyframe_pressed();
	void duplicate_keyframe_pressed();
	void delete_keyframe_pressed();
	*/

	void show_keyframe_properties();
	void keyframe_toggle();
	void keyframe_description_set();
	//animation render description change signal handler
	void refresh_rend_desc();

	//The manager of keyframes actions
	KeyframeActionManager* keyframe_action_manager;

protected:
	virtual void init_canvas_view_vfunc(etl::loose_handle<CanvasView> canvas_view);
	virtual void changed_canvas_view_vfunc(etl::loose_handle<CanvasView> canvas_view);

public:


	Dock_Keyframes();
	~Dock_Keyframes();
}; // END of Dock_Keyframes

}; // END of namespace studio

/* === E N D =============================================================== */

#endif
