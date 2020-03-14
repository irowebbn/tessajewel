---
layout: post-wide
hero-bg-color: "#000000"
uid: familial_code
title:  "Familial Code"
show: familial_code
categories: project
type: studio
medium: Mixed Media
permalink: /familialcode/
dates: 2020
poster: familial_code_poster
description: <p> Within the unique bond of family, we see many traditions reflected— unspoken bonds and feelings woven into our everyday lives. Seen in each member in our family, there are patterns that appear and reappear with time, a sort of ‘code’ . I come from an Appalachian tradition, so the acts of sewing, mending, embroidering, and quilting have been woven into me. These acts are part of the code given to me by my family, and the patterns we create with our textiles reflect these patterns within our family. Nature is a recurring theme in my work, suggesting it as the only earthly thing as constant in code as family and heritage.  Both family and nature are organic in their production, yet consistent in their structure.</p> <p> I display parts of both my family and myself in my work by using materials passed down to me from my relatives and using images originating from family trips and memories. I use embroidery techniques such as cross-stitch and punch needling to embellish these images, and by using multiple sewing techniques I pay homage to the traditional work of cross-stitch samplers that are used to showcase a wide array of stitch techniques. Braille is used on my  three-dimensional pieces, as a tactile way to announce these themes we see in family tradition without it being as clearly spelled out, inviting us to touch and feel these deep emotions. </p>
---


<ul class="projects clearfix">
{% for post in site.posts %}
{% if post.show == "familial_code"%}
  <li>
    <div class="project">
      <a class="cover" href="{{ post.url }}">
        <div class="project-details">
          <span>
            View photo
          </span>
        </div>
      </a>
      <img class="thumb" src="{{site.baseurl}}img/{{post.type}}/{{post.show}}/{{ post.uid }}.jpg" />
      <div class="aspect-two-one"></div>
    </div>
  </li>
{% endif %}
{% endfor %}
</ul>