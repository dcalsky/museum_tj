/**
 * Created by Dcalsky on 16/5/23.
 */

function Slider(container, nextContainer) {
    this.container = container
    this.next = nextContainer
    this.comments = []
    this.page = 0
}

Slider.prototype.loadMore = function () {
    this.page = this.page + 1
    $.ajax({
        url: '/comment/get',
        method: 'get',
        data: {page: this.page},
        success: function (result) {
            this.comments = result.content.comments
            console.log(this.comments)
        }
    })
}

Slider.prototype.init = function () {
    this.loadMore()
    this.next.click(this.loadMore.bind(this))
}


$(document).ready(function () {
    var slider = new Slider($('#comments-slider'), $('#next'))
    slider.init()
})