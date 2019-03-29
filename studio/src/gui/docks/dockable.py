#	file docks/dockable.py
#	Description: Template Header
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


#include <gtkmm/stockid.h>
#include <gtkmm/button.h>
#include <gtkmm/table.h>
#include <gtkmm/tooltip.h>
#include <gtkmm/label.h>
#include <gtkmm/frame.h>
#include <gtkmm/handlebox.h>
#include <gtkmm/box.h>
#include <gtkmm/scrolledwindow.h>
#include <gtkmm/toolbar.h>
#include <gtkmm/toolbutton.h>
import wx

#include "dialogsettings.h"
#include <synfig/string.h> => replaced with python inbuilt string


class DockManager:
	pass

class DockBook:
	pass

# class Dockable : public Gtk::Table
class Dockable:
	# Dockable::Dockable(const synfig::String& name,const synfig::String& local_name,
	# Gtk::StockID stock_id_):
	#  // Gtk::Window(Gtk::WINDOW_TOPLEVEL),
	# name_(name),
	# local_name_(local_name),
	#  // dialog_settings(this,name),
	# title_label_(local_name,Gtk::ALIGN_START),
	# stock_id_(stock_id_)
	def __init__(self, name, local_name, stock_id):
		scrolled_= 0
		use_scrolled_= True
		attach_dnd_to(title_label_)
		
		toolbar_ = 0

		table = wx.Grid
	
	Gtk::Table* table(this);

	{
		title_label_.set_padding(0,0);
		//title_label_.show();
		Gtk::EventBox* event_box(manage(new Gtk::EventBox()));
		event_box->set_border_width(0);
		event_box->add(title_label_);
		//table->attach(*event_box, 0, 1, 0,1, Gtk::EXPAND|Gtk::FILL, Gtk::SHRINK|Gtk::FILL, 0, 0);

		header_box_.pack_start(*event_box);

		attach_dnd_to(*event_box);
		event_box->show();
	//	event_box->set_events(Gdk::ALL_EVENTS_MASK); //!< \todo change this to only allow what is necessary for DnD


		Gtk::Button* bttn_close(manage(new Gtk::Button(_("X"))));
		//table->attach(*bttn_close, 1, 2, 0,1, Gtk::SHRINK|Gtk::FILL, Gtk::SHRINK|Gtk::FILL, 0, 0);
		header_box_.pack_end(*bttn_close,false,false);
		bttn_close->show();
		bttn_close->set_relief(Gtk::RELIEF_NONE);
		bttn_close->signal_clicked().connect(
				sigc::bind(sigc::ptr_fun(&DockManager::remove_widget_by_pointer_recursive), this));
		bttn_close->set_border_width(0);
		dynamic_cast<Gtk::Misc*>(bttn_close->get_child())->set_padding(0,0);
	}

	prev_widget_=manage(new Gtk::Label(" "));

	//table->attach(header_box_, 0, 1, 0,1, Gtk::SHRINK|Gtk::FILL, Gtk::SHRINK|Gtk::FILL, 0, 0);
	table->attach(*prev_widget_, 0, 1, 1,2, Gtk::EXPAND|Gtk::FILL, Gtk::EXPAND|Gtk::FILL, 0, 0);
	//table->attach(*toolbar_, 0, 1, 2,3, Gtk::EXPAND|Gtk::FILL, Gtk::SHRINK|Gtk::FILL, 0, 0);
	set_toolbar(*manage(new Gtk::Toolbar));
	table->show();

	prev_widget_->show();

	set_size_request(175,120);

##############

	friend class DockManager;
	friend class DockBook;


	sigc::signal<void> signal_stock_id_changed_;
	sigc::connection prev_widget_delete_connection;
protected:

//	DialogSettings dialog_settings;


private:

	Gtk::Toolbar *toolbar_;

	synfig::String name_;
	synfig::String local_name_;
	Gtk::Frame frame_;
	Gtk::Label title_label_;
	//Gtk::HBox button_box_;
	Gtk::HBox header_box_;

	//Gtk::HandleBox handle_box_;
	Gtk::ScrolledWindow *scrolled_;
	Gtk::Widget *prev_widget_;

	bool use_scrolled_;

	Gtk::StockID stock_id_;

	bool dnd_success_;

public:

	void set_toolbar(Gtk::Toolbar& toolbar);

	void set_use_scrolled(bool x) { use_scrolled_=x; }

	Dockable(const synfig::String& name,const synfig::String& local_name,Gtk::StockID stock_id_=Gtk::StockID(" "));
	~Dockable();

	sigc::signal<void>& signal_stock_id_changed() { return signal_stock_id_changed_; }

	const synfig::String& get_name()const { return name_; }
	const synfig::String& get_local_name()const { return local_name_; }

	const Gtk::StockID& get_stock_id()const { return stock_id_; }
	void set_stock_id(Gtk::StockID x) { stock_id_=x; signal_stock_id_changed()(); }

	void set_local_name(const synfig::String&);

	void clear();

	//DialogSettings& settings() { return dialog_settings; }
	//const DialogSettings& settings()const { return dialog_settings; }

	void add(Gtk::Widget& x);

	Gtk::ToolButton* add_button(const Gtk::StockID& stock_id, const synfig::String& tooltip=synfig::String());

	virtual void present();

	void attach_dnd_to(Gtk::Widget& widget);

	bool clear_previous();
	virtual Gtk::Widget* create_tab_label();

private:

	void on_drag_data_get(const Glib::RefPtr<Gdk::DragContext>&, Gtk::SelectionData& selection_data, guint info, guint time);
	void on_drag_end(const Glib::RefPtr<Gdk::DragContext>&context);
	void on_drag_begin(const Glib::RefPtr<Gdk::DragContext>&context);
	void on_drag_data_received(const Glib::RefPtr<Gdk::DragContext>& context, int, int, const Gtk::SelectionData& selection_data, guint, guint time);
