$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#add_asset').modal("show");
                },
                success:function(data){
                    $("#add_asset .modal-content").html(data.html_form);
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
                    $("#asset-table tbody").html(data.model_list);
                    $('#add_asset').modal("hide");
                }
                else {
                    $("#add_asset .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#add_asset").on("submit",".asset_create_from",saveForm);
    
    // edit
    $("#asset-table").on("click",".js-update",loadForm);
    $("#add_asset").on("submit",".asset_save_from",saveForm);

    // delete
    $("#asset-table").on("click",".js-delete",loadForm);
    $("#add_asset").on("submit",".asset_delete_from",saveForm);

});

