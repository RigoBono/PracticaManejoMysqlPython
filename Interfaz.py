import gtk


class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Libreria")
        self.set_size_request(600, 300)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)

        mb = gtk.MenuBar()

        filemenu = gtk.Menu()
        filem = gtk.MenuItem("Libro")
        filem.set_submenu(filemenu)
       
        VerTodos = gtk.MenuItem("Ver Todos")
        VerTodos.connect("activate", gtk.main_quit)
        filemenu.append(VerTodos)

	Anadir = gtk.MenuItem("Anadir libro")
        Anadir.connect("activate", gtk.main_quit)
        filemenu.append(Anadir)

	ModificaLibro = gtk.MenuItem("Modificar informacion de un libro")
        ModificaLibro.connect("activate", gtk.main_quit)
        filemenu.append(ModificaLibro)

        mb.append(filem)

	filem = gtk.MenuItem("Ayuda")
        filem.set_submenu(filemenu)
       
        VerTodos = gtk.MenuItem("Ver Todos")
        VerTodos.connect("activate", gtk.main_quit)
        filemenu.append(VerTodos)

	Anadir = gtk.MenuItem("Anadir libro")
        Anadir.connect("activate", gtk.main_quit)
        filemenu.append(Anadir)

	ModificaLibro = gtk.MenuItem("Modificar informacion de un libro")
        ModificaLibro.connect("activate", gtk.main_quit)
        filemenu.append(ModificaLibro)

        mb.append(filem)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
        
PyApp()
gtk.main()
