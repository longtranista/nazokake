function abbreviateNumber(value) {
    var newValue = value;
    if (value >= 1000) {
        var suffixes = ["", "k", "m", "b","t"];
        var suffixNum = Math.floor( (""+value).length/3 );
        var shortValue = '';
        for (var precision = 2; precision >= 1; precision--) {
            shortValue = parseFloat( (suffixNum != 0 ? (value / Math.pow(1000,suffixNum) ) : value).toPrecision(precision));
            var dotLessShortValue = (shortValue + '').replace(/[^a-zA-Z 0-9]+/g,'');
            if (dotLessShortValue.length <= 2) { break; }
        }
        if (shortValue % 1 != 0)  shortNum = shortValue.toFixed(1);
        newValue = shortValue+suffixes[suffixNum];
    }
    return newValue;
}


function template(posts) {
var tmpl = '';
for (var i = 0; i < posts.length ; i++ ) {
  var post = posts[i];
  tmpl += [
  '<div class="item" id="' + post.id + '">',
  '<p>',
  '<span class="highlight">' + post.kakeru + '</span>　とかけて　<span class="highlight">' + post.toku + '</span> と解きます',
  '</p>',
  '<p>',
  'その心は？　　どちらも　<span class="highlight orange"> <span class="blur">答えを見る</span><span class="answer hidden">' + post.kokoro + '</span></span>',
  '</p>',
  '<p class="right" >',
  '<a class="twitter-share-button" href="https://twitter.com/intent/tweet?text=' + post.share_text + '"> <i class="fa fa-twitter" aria-hidden="true"></i>Tweet</a>',
  '<span class="liked-number" count="' + post.like + '">' + post.like + '</span>',
  '<a href="javascript:void(0);" id="' + post.id + '" class="like-btn"><i class="fa fa-heart-o" aria-hidden="true"></i> like</a>',
  '</p>',
  '</form>',
  '</div>'
  ].join('');
}
return tmpl;
}

function syncLikeBtn() {
    $('.like-btn').each(function () {
      var id =  $(this).attr('id');
      var key = 'id-' + id;
      var me = this;
      if($.cookie(key)) {
        $(me).find('i').removeClass('fa-heart-o').addClass('fa-heart');
      }
    })

    $('.liked-number').each(function () {
      $(this).text(abbreviateNumber(parseInt($(this).attr('count'))));
    })
}


$(document).ready(function () {

    syncLikeBtn();

    $('.post-list').on('click', '.like-btn', function () {
      var id =  $(this).attr('id');
      var key = 'id-' + id;
      var me = this;
      var likecount = parseInt($(me).siblings('.liked-number').attr('count'));
      if ($.cookie(key) === undefined){
        NProgress.start()
        $.get('/api/like?id=' + id, {}, function (res) {
          $.cookie(key, true);
          $(me).find('i').removeClass('fa-heart-o').addClass('fa-heart');
          $(me).siblings('.liked-number').text(abbreviateNumber(++likecount)).attr('count', likecount);
          NProgress.done();
        })
      }else {
        $.removeCookie(key);
        $(me).find('i').removeClass('fa-heart').addClass('fa-heart-o');
        $(me).siblings('.liked-number').text(abbreviateNumber(--likecount)).attr('count', likecount);
      }
      
    });

    $('.post-list').on('click', '.blur', function () {
      var $me = $(this);
      var $next = $(this).siblings('.answer');
      $me.addClass('hidden');
      $next.removeClass('hidden');
    });

    $('.post-cover').click(function () {
      $(this).siblings('form').removeClass('hidden-sm hidden-xs');
      $(this).hide();
    })

    $(window).scroll(function() {
       if($(window).scrollTop() + $(window).height() == $(document).height()) {
          var pageMode = $('#pageMode').val();
          NProgress.start()
          $.get('/api/load?count=' + $('.item').length + '&mode=' + pageMode, {}, function (res) {
            
            $('.post-list').append(template(res.posts));

            syncLikeBtn();

            NProgress.done()
          })
       }
    });

})