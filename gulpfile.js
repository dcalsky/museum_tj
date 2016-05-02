var gulp = require('gulp'),
    stylus = require('gulp-stylus'),
    poststylus = require('poststylus');

gulp.watch('static/**/*.styl', function(event) {
    gulp.src(event.path, {base: 'static'})
    .pipe(stylus({
      use: [
        poststylus(['autoprefixer', 'rucksack-css'])
      ]
    }))
    .pipe(gulp.dest('static'))
    console.log('change: ' + event.path)
});

gulp.task('default', function () {
    console.log('watching styles')
});