$("#formulario1").validate({
    rules: {
        "txtNombre": {
            required: true,
            minlength: 3
        },
        "txtApellido": {
            required: true,
            minlength: 3
        },
        "txtEmail": {
            required: true,
            email: true
        },
        "txtContrasena": {
            required: true,
            minlength: 5
        },
        "txtRepetirContrasena": {
            required: true,
            equalTo: '#id_txtContrasena'
        }
    }, // --> Fin de reglas
    messages: {
        "txtNombre": {
            required: 'Ingrese Nombre',
            minlength: 'Min. 3 caract'
        },
        "txtApellido": {
            required: 'Ingrese Apellido',
            minlength: 'Min. 3 caract'
        },
        "txtEmail": {
            required: 'Ingrese email',
            email: 'No cumple formato'
        },
        "txtContrasena": {
            required: 'Ingrese Contraseña',
            minlength: 'Min. 5 caract'
        },
        "txtRepetirContrasena": {
            required: 'Repita la Contraseña',
            equalTo: ' Las contraseñas deben ser identicas'
        }
    } //-->Fin de mensajes

});

$("#btn-registrar").click(function(e) {
    e.preventDefault(); // Evita que se envíe el formulario automáticamente

    // Verificar si el formulario es válido
    if ($("#formulario1").valid()) {
        // Si el formulario es válido, redirigir al usuario al inicio
        window.location.href = 'index.html';
    }
});