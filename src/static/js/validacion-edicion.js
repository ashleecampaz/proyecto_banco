function validarCampoObligatorio(campo, errorElement, mensaje) {
    if (campo.value.trim() === '') {
        errorElement.textContent = mensaje;
        return false;
    } else {
        errorElement.textContent = '';
        return true;
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

    inputCedula.addEventListener('blur', () => validarCampoObligatorio(inputCedula, labelErrorCedula,'El campo esta vacio'));
    inputNombre.addEventListener('blur', () => validarCampoObligatorio(inputNombre, labelErrorNombre,'El nombre es obligatorio'));  
    inpuApellido.addEventListener('blur', () => validarCampoObligatorio(inpuApellido, labelErrorApellido,'El apellido es obligatorio'));  
    inputCelular.addEventListener('blur', () => validarCampoObligatorio(inputCelular, labelErrorCelular,'El celular es obligatorio'));  
    
}

function validarConsulta(){
    const inputCedula =  document.getElementById('cedula-usuario');
    cedulaValida =   validarCampoObligatorio(inputCedula, labelErrorCedula,'La cedula es obligatoria');

    // Si todas las validaciones son correctas, se devuelve true y se puede enviar el formulario al servidor
    if (cedulaValida) {
        const formulario = document.getElementById('formulario-consulta'); 
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

function validarEdicion(){
    const inputNombre= document.getElementById('nombre-usuario');
    const inpuApellido = document.getElementById('apellido-usuario');
    const inputCelular= document.getElementById('celular-usuario');

    const labelErrorNombre=document.getElementById('error-nombre');
    const labelErrorApellido=document.getElementById('error-apellido');
    const labelErrorCelular=document.getElementById('error-celular');


    nombreValido = validarCampoObligatorio(inputNombre, labelErrorNombre,'El nombre es obligatorio');  
    apellidoValido = validarCampoObligatorio(inpuApellido, labelErrorApellido,'El apellido es obligatorio');  
    celularValido = validarCampoObligatorio(inputCelular, labelErrorCelular,'El celular es obligatorio'); 

    // Si todas las validaciones son correctas, se devuelve true y se puede enviar el formulario al servidor
    if ( apellidoValido && nombreValido  && celularValido) {
        const formulario = document.getElementById('formulario-edicion'); 
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
function validaciones(){
    document.getElementById('boton-guardar').addEventListener('click',validarConsulta); 
    document.getElementById('boton-eliminar').addEventListener('click',validarEdicion); 
    validarCamposAlCambiarFoco();
}


document.addEventListener('DOMContentLoaded', validaciones);


