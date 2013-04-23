from django_assets import Bundle, register

# css
base_css = Bundle(
    'css/bootstrap/bootstrap.min.css',
    'css/bootstrap/bootstrap-responsive.min.css',
    'css/jquery-ui.css',
    'css/chosen.css',
    )

project_css = Bundle(
    'css/project.scss',
    filters='pyscss,cssmin',
    )

register('styles', Bundle(base_css, project_css, output='css/style.css'))

# js
base_js = Bundle(
    'js/jquery/jquery.min.js',
    'js/jquery/jquery-ui.min.js',
    'js/jquery/jquery.numeric.min.js',
    'js/jquery/jquery.chosen.min.js',
    'js/bootstrap/bootstrap.min.js',
    'js/underscore/underscore-min.js',
    )

project_js = Bundle(
    'js/project.coffee',
    filters='coffeescript',
)

register('scripts', Bundle(base_js, project_js, output='js/scripts.js'))
