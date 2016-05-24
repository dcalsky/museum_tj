/**
 * Created by Dcalsky on 16/5/23.
 */

var INITIAL_PAGE = 1
var NEXT_PAGE = 1
var PREV_PAGE = -1

function Slider(container, next, prev) {
    this.container = container
    this.nextContainer = next
    this.prevContainer = prev
    this.comments = []
    this.page = 0
}

Slider.prototype.next = function() {
    this.load(NEXT_PAGE)
}

Slider.prototype.prev = function() {
    this.load(PREV_PAGE)
}

Slider.prototype.load = function (diff) {
    var container = this.container
    this.page = this.page + diff
    $.ajax({
        url: '/comment/get',
        method: 'get',
        data: {page: this.page},
        success: function (result) {
            var comments = result.content.comments
            var commentsElement = '<ul>'
            comments.map(function(comment) {
                console.log(comment)
                commentsElement += '<li>\
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
            commentsElement += '</ul>'
            container.html(commentsElement)
        }
    })
}

Slider.prototype.init = function () {
    this.load(INITIAL_PAGE)
    this.nextContainer.click(this.next.bind(this))
    this.prevContainer.click(this.prev.bind(this))
}


$(document).ready(function () {
    var slider = new Slider($('#comments-slider'), $('#next'), $('#prev'))
    slider.init()
})