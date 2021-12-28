$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#add_training').modal("show");
                },
                success:function(data){
                    $("#add_training .modal-content").html(data.html_form);
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
                    $("#training-table tbody").html(data.model_list);
                    $('#add_training').modal("hide");
                }
                else {
                    $("#add_training .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#add_training").on("submit",".training_create_from",saveForm);
    
    // edit
    $("#training-table").on("click",".js-update",loadForm);
    $("#add_training").on("submit",".training_save_from",saveForm);

    // delete
    $("#training-table").on("click",".js-delete",loadForm);
    $("#add_training").on("submit",".training_delete_from",saveForm);

});

