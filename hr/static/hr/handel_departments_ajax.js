$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#edit_department').modal("show");
                },
                success:function(data){
                    $("#edit_department .modal-content").html(data.html_form);
                }
            })
    };
    

    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            data:form.serialize(),
            type:form.attr('method'),
            dataType:'json',
            success: function (data){
                if(data.form_is_valid){
                    $("#departments-table tbody").html(data.model_list);
                    $('#edit_department').modal("hide");
                }
                else {
                    $("#edit_department .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#edit_department").on("submit",".department_create_from",saveForm);
    
    // edit
    $("#departments-table").on("click",".js-update",loadForm);
    $("#edit_department").on("submit",".department_save_from",saveForm);

    // delete
    $("#departments-table").on("click",".js-delete",loadForm);
    $("#edit_department").on("submit",".department_delete_from",saveForm);

});

