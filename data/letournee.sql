///Local
create database letournee;

use letournee;

create table user(
id_user mediumint(8) not null auto_increment,
name varchar(30) not null,
ap_paterno varchar(30) not null,
ap_materno varchar(30) not null,
account_name varchar(10) not null,
age int(8) not null,
email varchar(30) not null,
password varchar(20) not null,
imagen_usuario varchar(400),
primary key (id_user)
);


create table pueblos(
    id_pueblo mediumint(8) not null auto_increment primary key,
    nom_pueblo varchar(30) not null,
    descripcion  text(400) not null,
    imagen_pueblo varchar(100) null
);


create table imagenes(
    id_imagen mediumint(8) not null auto_increment primary key,
    imagen varchar(100) not null,
    id_pueblo mediumint(8) not null,
    foreign key(id_pueblo) references pueblos(id_pueblo)
);

create table lugares_interes(
    id_lugar_interes mediumint(8) not null auto_increment primary key,
    nombre varchar(60) not null,
    descripcion varchar(300) not null,
    id_imagen mediumint(8) not null,
    id_pueblo mediumint(8) not null,
    foreign key(id_pueblo) references pueblos(id_pueblo),
    foreign key(id_imagen) references imagenes(id_imagen)
);



insert into user(name,ap_paterno,ap_materno,account_name, age, email, password) values('Diego David','Hernandez','Lopez','DDHL97',19,'1715110005@utec-tgo.edu.mx','cocomo');


------------------------------------------
formLog = web.form.Form(
        web.form.Textbox('account_name',web.form.notnull,
                        size = 30,
                        decription="Nombre usuario"),
        web.form.Textbox('password',web.form.notnull,
                        size = 30,
                        decription="Contrasenia"),
        web.form.Button('Registrarse')
    )
    
    login.html
    $def with (form)

<div class="container">
    <div class="row">
        <div class="col-md-5 col-md-offset-3">
            <div class="page-header text center">
                <h1>Ejemplo de login</h1>       
            </div>
                <form action="" method="post" enctype="multipart/form-data" class="form-signin">
                        $:form.render()
                </form>
               </div>
    </div>
</div>
