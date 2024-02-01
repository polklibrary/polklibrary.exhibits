

$(document).ready(function(){


    // Editor Helper
    if ($('body').is('.portaltype-polklibrary-exhibits-models-exhibit')) {
    
        $('#formfield-form-widgets-js').hide()
        .after($('<div>').attr('id','editor-js').css({'height':'400px','width':'80%','margin':'0 10px 10px 10px','border':'1px solid #666'}))
        .after($('<label>').html('Javascript (Added to every item in this exhibit, jquery is added already)').css({'margin':'10px'}));
        $('#formfield-form-widgets-js').find('textarea').addClass('editor-js');
        
        $('#formfield-form-widgets-css').hide()
        .after($('<div>').attr('id','editor-css').css({'height':'400px','width':'80%','margin':'0 10px 10px 10px','border':'1px solid #666'}))
        .after($('<label>').html('CSS (Added to every item in this exhibit)').css({'margin':'10px'}));
        $('#formfield-form-widgets-css').find('textarea').addClass('editor-css');
        
        var load_ace = function(){
            
            // JS         
            var js_textarea = $('.editor-js');
            var editor_js = ace.edit('editor-js');
            editor_js.setTheme("ace/theme/chrome");
            editor_js.getSession().setMode("ace/mode/javascript");
            editor_js.getSession().setValue(js_textarea.val());
            editor_js.getSession().on('change', function(){
                js_textarea.val(editor_js.getSession().getValue());
            });
            
            //CSS
            var css_textarea = $('.editor-css');
            var editor_css = ace.edit('editor-css');
            editor_css.setTheme("ace/theme/chrome");
            editor_css.getSession().setMode("ace/mode/css");
            editor_css.getSession().setValue(css_textarea.val());
            editor_css.getSession().on('change', function(){
                css_textarea.val(editor_css.getSession().getValue());
                $("#formfield-form-widgets-body iframe").contents().find("head").find(".active-edits").remove();
                $("#formfield-form-widgets-body iframe").contents().find("head").append(
                    '<style class="active-edits">' + editor_css.getSession().getValue() + '</style>'
                );
                
            });
            
        }
        
        var script = $('<script>').attr('type','text/javascript').attr(
            'src', $('body').attr('data-portal-url') + '/++plone++static/components/ace-builds/src/ace.js'
        );
        $('head').append(script);
        var ace_thread = setInterval(function(){
            if (typeof ace !== 'undefined') {
                load_ace();
                clearInterval(ace_thread);
                ace_thread = null;
            }
        },250);
    
    }


});