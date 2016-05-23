/**
 * Created by Dcalsky on 16/5/23.
 */

function Slider(container, nextContainer) {
    this.container = container
    this.next = nextContainer
}

Slider.prototype.loadMore = function() {
    console.log('next')
    // todo ajax
}

Slider.prototype.init = function () {
    // todo ajax
    this.next.click(this.loadMore)
}


$(document).ready(function () {
    var slider = new Slider($('#comments-slider'), $('#next'))
    slider.init()
})