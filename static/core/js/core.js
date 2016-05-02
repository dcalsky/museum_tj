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
    slider.init()

})