var gulp = require('gulp'),
    stylus = require('gulp-stylus'),
    poststylus = require('poststylus');


function handleStylus(path) {
    path = path || 'static/**/*.styl'
    gulp.src(path, {base: 'static'})
    .pipe(stylus({
      use: [
        poststylus(['autoprefixer', 'rucksack-css'])
      ]
    }))
    .pipe(gulp.dest('static'))
}

gulp.task('stylus', function () {
    handleStylus()
})

gulp.watch('static/**/*.styl', function (event) {
    handleStylus(event.path)
    console.log('change: ' + event.path)
})

gulp.task('default', ['stylus'])