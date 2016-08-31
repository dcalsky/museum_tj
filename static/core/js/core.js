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

var jumpToArticle = function (num) {
    switch (num) {
        case 1:
            window.location.href = '/museum/part/guide/8'
            break
        case 2:
            window.location.href = '/museum//part/guide/9'
            break
        case 3:
            window.location.href = '/museum/part/guide/10'
            break
    }
}

$(document).ready(function () {
    var page = 2
    var slider = new Slider($('#slider'))
    var newsSlider = new Slider($('#news-slider'))
    slider.init()
    newsSlider.init()
    $('#load-more').click(function () {
        $.ajax({
            url: '/' + page,
            success: function (res) {
                console.log(res)
            }
        })
    })
    // $('#floor li').click(function () {
    //     console.log(e)
    // })
})