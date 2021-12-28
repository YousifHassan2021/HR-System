$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#edit_designation').modal("show");
                },
                success:function(data){
                    $("#edit_designation .modal-content").html(data.html_form);
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
                    $("#overtime-table tbody").html(data.model_list);
                    $('#edit_designation').modal("hide");
                }
                else {
                    $("#edit_designation .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#edit_designation").on("submit",".overtime_create_from",saveForm);
    
    // edit
    $("#overtime-table").on("click",".js-update",loadForm);
    $("#edit_designation").on("submit",".overtime_save_from",saveForm);

    // delete
    $("#overtime-table").on("click",".js-delete",loadForm);
    $("#edit_designation").on("submit",".overtime_delete_from",saveForm);

});

