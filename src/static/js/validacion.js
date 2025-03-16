function validarCampoObligatorio(campo, errorElement, mensaje) {
    if (campo.value.trim() === '') {
        errorElement.textContent = mensaje;
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function mostrarMensajeExito() {
    Toastify({
        text: "✅ ¡Registro exitoso!",
        duration: 3000,            // Duración: 3 segundos
        gravity: "top",             // Posición: arriba
        position: "right",          // Alineación: derecha
        style: {
            background: "rgba(0, 128, 0, 0.8)",  // Verde con transparencia
            color: "#fff",                      // Texto blanco
            borderRadius: "12px",               // Esquinas redondeadas
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.3)", // Sombra ligera
            padding: "12px 20px"               // Más relleno
        },
        stopOnFocus: true, // No desaparecer al pasar el mouse
    }).showToast();
}

// Función principal que valida todo el formulario
function validarFormulario() {

    const inputCedula =  document.getElementById('cedula-usuario');
    const inputNombre= document.getElementById('nombre-usuario');
    const inpuApellido = document.getElementById('apellido-usuario');
    const inputCelular= document.getElementsByName('celular-usuario');

    const labelErrorCedula=document.getElementById('error-cedula');
    const labelErrorNombre=document.getElementById('error-nombre');
    const labelErrorApellido=document.getElementById('error-apellido');
    const labelErrorCelular=document.getElementById('error-celular');


    cedulaValida =   validarCampoObligatorio(inputCedula, labelErrorCedula,'La cedula es obligatoria');
    nombreValido = validarCampoObligatorio(inputNombre, labelErrorNombre,'El nombre es obligatorio');  
    apellidoValido = validarCampoObligatorio(inpuApellido, labelErrorApellido,'El apellido es obligatorio');  
    celularValido = validarCampoObligatorio(inputCelular, labelErrorCelular,'El celular es obligatorio');  

    // Si todas las validaciones son correctas, se devuelve true y se puede enviar el formulario al servidor
    if (cedulaValida && apellidoValido && nombreValido  && celularValido) {
        mostrarMensajeExito(); 
        const formulario = document.getElementById('formulario-usuario'); 
        document.documentElement.scrollIntoView({ behavior: "smooth", block: "start" });   
        setTimeout(() => {
            formulario.reset();
        }, 2000);
        return True;
    } else {
       
        alert('Por favor, complete correctamente el formulario.');
        return false; // Bloquea el envío del formulario
    }

}

function validarCamposAlCambiarFoco()
{

    const inputCedula =  document.getElementById('cedula-usuario');
    const inputNombre= document.getElementById('nombre-usuario');
    const inpuApellido = document.getElementById('apellido-usuario');
    const inputCelular= document.getElementById('celular-usuario');

    const labelErrorCedula=document.getElementById('error-cedula');
    const labelErrorNombre=document.getElementById('error-nombre');
    const labelErrorApellido=document.getElementById('error-apellido');
    const labelErrorCelular=document.getElementById('error-celular');

    inputCedula.addEventListener('blur', () => validarCampoObligatorio(inputCedula, labelErrorCedula,'La cedula es obligatoria'));
    inputNombre.addEventListener('blur', () => validarCampoObligatorio(inputNombre, labelErrorNombre,'El nombre es obligatorio'));  
    inpuApellido.addEventListener('blur', () => validarCampoObligatorio(inpuApellido, labelErrorApellido,'El apellido es obligatorio'));  
    inputCelular.addEventListener('blur', () => validarCampoObligatorio(inputCelular, labelErrorCelular,'El celular es obligatorio'));  
    
}

function validaciones(){
    document.getElementById('boton-registrar').addEventListener('click',validarFormulario); 
    validarCamposAlCambiarFoco();
}


document.addEventListener('DOMContentLoaded', validaciones);


