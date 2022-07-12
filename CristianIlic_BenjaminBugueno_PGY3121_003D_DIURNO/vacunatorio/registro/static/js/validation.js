/* i want to do a validation on the form */
function validateForm() {

    nombre = document.form.txt_nombre.value
    appaterno = document.form.txt_appaterno.value
    apmaterno = document.form.txt_apmaterno.value
    rut = document.form.txt_rut.value
    edad = document.form.txt_edad.value
    nomvacuna = document.form.txt_vacuna.value
    fecha = document.form.txt_fecha.value
    nomvac = document.form.nom_vac.value
    dirvac = document.form.dir_vac.value
    tpvac = document.form.tp_vac.value
    telvac = document.form.tel_vac.value
    mailvac = document.form.mail_vac.value


    if (nombre.value().length<3)
   {
       alert("Nombre debe tener al menos 3 caracteres")
       document.form.txt_nombre.focus()
       e.preventDefault()

       
   }
   if (appaterno.value().length<3)
   {
       alert("Apellido paterno debe tener al menos 3 caracteres")
       document.form.txt_appaterno.focus()
       e.preventDefault()

   }
   if (apmaterno.value().length<3)
   {
       alert("Apellido materno debe tener al menos 3 caracteres")
       document.form.txt_apmaterno.focus()
       e.preventDefault()

       
   }

   if (rut.value()<9 && rut.value()>10 && rut.value().indexOf('-')<0)
   {
       alert("El rut debe tener entre 9 y 10 caracteres, sin puntos y debe contener un guión")
       document.form.txt_rut.focus()
       e.preventDefault()

   }



document.form.action = "/ingreso_registro/"
document.form.submit() = True
alert("Formulario enviado")


    
}

