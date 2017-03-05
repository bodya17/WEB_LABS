var gulp = require('gulp');
var rigger = require('gulp-rigger');

gulp.task('default', function () {
  gulp.src('src/*.html')
      .pipe(rigger())
      .pipe(gulp.dest('dest/'));
});

gulp.task('watch', function() {
  gulp.watch('src/*.html', ['default']);
})
