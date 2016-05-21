/**
 * Created by Dcalsky on 16/5/2.
 */

function Slider(container) {
    this.container = container
}

Slider.prototype.init = function () {
    this.container.unslider({
        infinite: true,
        nav: false
    })
}


$(document).ready(function () {
    var slider = new Slider($('#slider'))
    var newsSlider = new Slider($('#news-slider'))
    slider.init()
    newsSlider.init()
    $('#appoint-form form').submit(function(e) {
        e.preventDefault()
    })
})