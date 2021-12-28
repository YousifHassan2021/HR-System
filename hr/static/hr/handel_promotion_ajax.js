$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#add_promotion').modal("show");
                },
                success:function(data){
                    $("#add_promotion .modal-content").html(data.html_form);
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
                    $("#promotion-table tbody").html(data.model_list);
                    $('#add_promotion').modal("hide");
                }
                else {
                    $("#add_promotion .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#add_promotion").on("submit",".promotion_create_from",saveForm);
    
    // edit
    $("#promotion-table").on("click",".js-update",loadForm);
    $("#add_promotion").on("submit",".promotion_save_from",saveForm);

    // delete
    $("#promotion-table").on("click",".js-delete",loadForm);
    $("#add_promotion").on("submit",".promotion_delete_from",saveForm);

});

