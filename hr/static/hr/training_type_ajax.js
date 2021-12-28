$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#add_type').modal("show");
                },
                success:function(data){
                    $("#add_type .modal-content").html(data.html_form);
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
                    $("#training_type_table tbody").html(data.model_list);
                    $('#add_type').modal("hide");
                }
                else {
                    $("#add_type .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#add_type").on("submit",".training_type_create_from",saveForm);
    
    // edit
    $("#training_type_table").on("click",".js-update",loadForm);
    $("#add_type").on("submit",".training_type_save_from",saveForm);

    // delete
    $("#training_type_table").on("click",".js-delete",loadForm);
    $("#add_type").on("submit",".training_type_delete_from",saveForm);

});

