/**
 * Created by Dcalsky on 16/5/23.
 */

var INITIAL_PAGE = 1
var NEXT_PAGE = 1
var PREV_PAGE = -1
var TOP_STEP = 130
var INITIAL = true


function Slider(container, next, prev) {
    this.container = container
    this.nextContainer = next
    this.prevContainer = prev
    this.comments = []
    this.page = 1
    this.count = 0
}

Slider.prototype.next = function () {
    this.slide(NEXT_PAGE, '-=500px')
}

Slider.prototype.prev = function () {
    this.slide(PREV_PAGE, '+=500px')
}

Slider.prototype.slide = function (diff, distance) {
    // var commentsElement = $('.comment')
    var self = this
    this.page += diff
    self.load(diff)
}

Slider.prototype.load = function (diff, isInitial) {
    var container = this.container
    var containerWidth = container.width()
    $.ajax({
        url: '/comment/get',
        method: 'get',
        data: {page: this.page},
        success: function (result) {
            var comments = result.content.comments
            var commentsElement = ''
            comments.map(function (comment, i) {
                var arrow = i % 2 === 0 ? 'right' : 'left'
                commentsElement += '<li class="comment" style="top: ' + ((i * TOP_STEP) + 20 ) + 'px;' + arrow + ':' + containerWidth / 2 + 'px">\
                    <div class="point1" style="' + arrow + ':-15px"></div><div class="point2"  style="' + arrow + ':-8px"></div>\
                    <div class="title">\
                        ' + comment.title + '\
                    </div>\
                    <div class="create_time">\
                        ' + comment.create_time + '\
                    </div>\
                    <div class="content">\
                        ' + comment.content + '\
                    </div>\
                </li>'
            })
            container.html(commentsElement)
        }
    })
}

Slider.prototype.init = function () {
    this.load(INITIAL_PAGE, INITIAL)
    this.nextContainer.click(this.next.bind(this))
    this.prevContainer.click(this.prev.bind(this))
}


$(document).ready(function () {
    var slider = new Slider($('#comments-slider'), $('#next'), $('#prev'))
    slider.init()
})