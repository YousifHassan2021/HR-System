$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#create_project').modal("show");
                },
                success:function(data){
                    $("#create_project .modal-content").html(data.html_form);
                }
            })
    };
    

    $(".js-create").click(function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:'get',
            dataType:'json',
            beforeSend:function(){
                $('#create_project').modal("show");
            },
            success:function(data){
                $("#create_project .modal-content").html(data.html_form);
            }
        })
    })


    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            data:form.serialize(),
            type:form.attr('method'),
            dataType:'json',
            success: function (data){
                if(data.form_is_valid){
                    $("#projects-table").html(data.model_list);
                    $('#create_project').modal("hide");
                }
                else {
                    $("#create_project .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#create_project").on("submit",".project_create_from",saveForm);
    
    // edit
    $("#projects-table").on("click",".js-update",loadForm);
    $("#create_project").on("submit",".project_save_from",saveForm);

    // delete
    $("#projects-table").on("click",".js-delete",loadForm);
    $("#create_project").on("submit",".project_delete_from",saveForm);

});

