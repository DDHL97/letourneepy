import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View',
    '/viewpueblo/(\d+)', 'Viewpueblo',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
    '/editpueblo/(\d+)', 'Editpueblo',
    '/borrar/(\d+)','Borrar',
    '/registros', 'Registros',
    '/newpueblo', 'Newpueblo',
    '/usuarios', 'Usuarios',
    '/pueblos', 'Pueblos',
    '/about', 'About',
    '/login', 'Login',
    '/huasca', 'Huasca',
    '/real', 'Real',
    '/mineral', 'Mineral',
    '/huichapan', 'Huichapan',
    '/tecozautla','Tecozaultla'
    
)


### Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)


class Index:

    def GET(self):
        posts = model.get_posts()
        return render.index()

class About:

    def GET(self):
        return render.about()

class Huasca:

    def GET(self):
        return render.huasca()

class Pueblos:
    def GET(self):
        pueblos = model.get_pueblos()
        return render.pueblos(pueblos)    

class Usuarios:
    def GET(self):
        posts = model.get_posts()
        return render.usuarios(posts)
    
class Registros:

    def GET(self):
        posts = model.get_posts()
        return render.registros(posts)

class View:

    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)

class Viewpueblo:

    def GET(self, id):
        pueblo = model.get_pueblo(int(id))
        return render.viewpueblo(pueblo)

class Newpueblo:
    
    formp = web.form.Form(
        web.form.Textbox('nom_pueblo', web.form.notnull,
            size = 30,
            description = 'Nombre del Pueblo'),
        web.form.Textarea('descripcion', web.form.notnull,
            size = 900,
            description = 'Descripcion'),
        web.form.File('imagen_pueblo', web.form.notnull,
            size=100,
            description="Imagen del pueblo:"),
        web.form.Button('Registrarse')
    )
    def GET(self):
        form = self.formp()
        return render.newpueblo(form)
    def POST(self):
        formp = self.formp()
        imagenp = web.input(imagen_pueblo={})
        filedir = 'static/images'
        filepath = imagenp.imagen_pueblo.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
        #copiar archivo al servidor
        fout = open(filedir + '/'+ filename,'w')
        fout.write(imagenp.imagen_pueblo.file.read())
        fout.close()
        imagen_pueblo = filename
        if not formp.validates():
            return render.newpueblo(formp)
        model.insertar_pueblo(formp.d.nom_pueblo, formp.d.descripcion, imagen_pueblo)
        raise web.seeother('/pueblos')
        
class New:

    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull, 
            size=30,
            description="Nombre:"),
        web.form.Textbox('ap_paterno', web.form.notnull, 
            rows=8, cols=32,
            description="Apellido Paterno:"),
        web.form.Textbox('ap_materno', web.form.notnull, 
            size=30,
            description="Apellido Materno:"),
        web.form.Textbox('account_name', web.form.notnull, 
            size=30,
            description="Nombre de Usuario:"),
        web.form.Textbox('age', web.form.notnull, 
            size=30,
            description="Edad:"),
        web.form.Textbox('email', web.form.notnull, 
            size=30,
            description="Email:"),
        web.form.Textbox('password', web.form.notnull, 
            size=30,
            description="Contrasena:"),
        web.form.File('imagen_usuario', web.form.notnull,
            size=30,
            description="Imagen del usuario:"),
        web.form.Button('Registrarse')
    )
    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        imagen = web.input(imagen_usuario={})
        filedir = 'static/images'
        filepath = imagen.imagen_usuario.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
#copiar archivo al servidor
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_usuario.file.read())
        fout.close()
        imagen_producto = filename
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.name, form.d.ap_paterno,form.d.ap_materno, form.d.account_name, form.d.age,form.d.email,form.d.password, imagen_usuario)
        raise web.seeother('/')

class Borrar:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.borrar(post)
    
    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')
    
        
        

class Delete:

    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)


    def POST(self, id):
        form = New.form()
        imagen = web.input(imagen_usuario={})
        filedir = 'static/images'
        filepath = imagen.imagen_usaurio.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
#copiar archivo al servidor
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_usuario.file.read())
        fout.close()
        imagen_usuario = filename
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.name, form.d.ap_paterno, form.d.ap_materno, form.d.account_name, form.d.age, form.d.email, form.d.password, imagen_usuario)
        raise web.seeother('/')

class Editpueblo:
    def GET(self, id):
        pueblo = model.get_pueblo(int(id))
        form = Newpueblo.formp()
        form.fill(pueblo)
        return render.editpueblo(pueblo, form)


    def POST(self, id):
        form = Newpueblo.formp()
        imagen = web.input(imagen_pueblo={})
        filedir = 'static/images'
        filepath = imagen.imagen_pueblo.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
#copiar archivo al servidor
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_pueblo.file.read())
        fout.close()
        imagen_pueblo = filename
        pueblo = model.get_pueblo(int(id))
        if not form.validates():
            return render.editpueblo(pueblo, form)
        model.update_pueblo(int(id), form.d.nom_pueblo, form.d.descripcion, imagen_pueblo)
        raise web.seeother('/pueblos')

class Login:
    
    def GET(self):
        return render.login()
    
    #def POST(self, account_name, password):
        #authdb = mysql.connect('letournee.db')
    #    model.login(form.account_name, form.password)
        #if check: 
        #    session.loggedin = True
        #    session.account_name = account_name
    #    raise web.seeother('/usuarios')   
        #else: 
        #     return render.base("Those login details don't work.")



                                
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()