function listadoUsuarios(){
    $.ajax({
        url: "/usuarios/listado_usuarios/",
        type:"get",
        dataType: "json",
        success: function(response){
            if ($.fn.DataTable.isDataTable('#myTable')){
                $('#myTable').DataTable().destroy();
            } 
            
                $('#myTable tbody').html("");
                for(let i = 0; i < response.length; i++){
                        let fila = '<tr>';
                        fila += '<td>' + (i + 1) + '</td>';
                        fila += '<td>' + response[i]["fields"]['username']+'</td>';
                        fila += '<td>' + response[i]["fields"]['nombres']+'</td>';
                        fila += '<td>' + response[i]["fields"]['apellidos']+'</td>';
                        fila += '<td>' + response[i]["fields"]['email']+'</td>';
                        fila += '<td>' + '<button type="button" class="btn btn-primary btn-sm tableButton"'
                        fila += ' onclick="abrir_modal_edicion(\'/usuarios/actualizar_usuarios/'+response[i]['pk']+'/\');">Editar</button>'
                        fila += '<button type="button" class="btn btn-danger btn-sm tableButton" '
                        fila += ' onclick="abrir_modal_edicion(\'/usuarios/eliminar_usuarios/'+response[i]['pk']+'/\');" >Eliminar</button>'+'</td>';


                        fila += '</tr>';
                        $('#myTable tbody').append(fila);
                };
                $('#myTable').DataTable({
                    "language": {
                        "decimal": "",
                        "emptyTable": "No hay información",
                        "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                        "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                        "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                        "infoPostFix": "",
                        "thousands": ",",
                        "lengthMenu": "Mostrar _MENU_ Entradas",
                        "loadingRecords": "Cargando...",
                        "processing": "Procesando...",
                        "search": "Buscar:",
                        "zeroRecords": "Sin resultados encontrados",
                        "paginate": {
                            "first": "Primero",
                            "last": "Ultimo",
                            "next": "Siguiente",
                            "previous": "Anterior"
                        },
                    }
                });
                
        },
        error: function(error){
            console.log(error);
        }
    });
}

function registrar(){
    activar_boton();
	$.ajax({
		data: $('#form_creacion').serialize(),
		url: $('#form_creacion').attr('action'),
		type: $('#form_creacion').attr('method'),
		success: function(response){
            notificacionSuccess(response.mensaje);
			listadoUsuarios();
			cerrar_modal_creacion();
		},
		error: function(error){
            notificacionError(error.responseJSON.mensaje);
			mostrarErroresEdicion(error);
            activar_boton();
		}
	});
};

function activar_boton(){
	if($('#boton_creacion').prop('disabled')){
		$('#boton_creacion').prop('disabled', false);
	} else{
		$('#boton_creacion').prop('disabled', true);
	}
};

function editar(){
    activar_boton();
    $.ajax({
		data: $('#form_edicion').serialize(),
		url: $('#form_edicion').attr('action'),
		type: $('#form_edicion').attr('method'),
		success: function(response){
            notificacionSuccess(response.mensaje);
			listadoUsuarios();
			cerrar_modal_edicion();
		},
		error: function(error){
            notificacionError(error.responseJSON.mensaje);
			mostrarErroresCreacion(error);
            activar_boton();
		}
	});
};
function eliminar(pk){
    activar_boton();
    $.ajax({
        data: {
            csrfmiddlewaretoken:($("[name='csrfmiddlewaretoken']").val())
        } ,
		url: '/usuarios/eliminar_usuarios/'+pk+'/',
		type: 'post',
		success: function(response){
            notificacionSuccess(response.mensaje);
			listadoUsuarios();
			cerrar_modal_edicion();
		},
		error: function(error){
            notificacionError(error.responseJSON.mensaje);
		}
	});
};
$(document).ready(function (){
    listadoUsuarios();
});