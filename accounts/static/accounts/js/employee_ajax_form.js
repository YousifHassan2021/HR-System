$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#add_employee').modal("show");
                },
                success:function(data){
                    $("#add_employee .modal-content").html(data.html_form);
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
                    $("#employee-table").html(data.model_list);
                    $('#add_employee').modal("hide");
                }
                else {
                    $("#add_employee .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#add_employee").on("submit",".employee_create_from",saveForm);
    
    // edit
    $("#employee-table").on("click",".js-update",loadForm);
    $("#add_employee").on("submit",".employee_save_from",saveForm);

    // delete
    $("#employee-table").on("click",".js-delete",loadForm);
    $("#add_employee").on("submit",".employee_delete_from",saveForm);

});

