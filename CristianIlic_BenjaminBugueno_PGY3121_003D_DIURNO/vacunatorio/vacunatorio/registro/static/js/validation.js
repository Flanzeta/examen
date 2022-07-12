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


    if (nombre.length < 3) {
        alert("Nombre debe tener al menos 3 caracteres")
        document.form.txt_nombre.focus()

        return false;


    }
    if (appaterno.length < 3) {
        alert("Apellido paterno debe tener al menos 3 caracteres")
        document.form.txt_appaterno.focus()

        return false;


    }
    if (apmaterno.length < 3) {
        alert("Apellido materno debe tener al menos 3 caracteres")
        document.form.txt_apmaterno.focus()

        return false;


    }

    if (rut < 9 && rut > 10 && rut.indexOf('-') < 0) {
        alert("El rut debe tener entre 9 y 10 caracteres, sin puntos y debe contener un guión")
        document.form.txt_rut.focus()

        return false;


    }



    document.form.action = "/ingreso_registro/"
    document.form.submit() = true
    alert("Formulario enviado")

}

