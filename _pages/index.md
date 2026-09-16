
---

---

<p>从 <a class="internal-link" href="{{ site.baseurl }}/🍀 花园导览/🍀 花园导览.md">🍀 花园导览</a> 开始逛这个花园。下面只是时间线，不是地图。</p>

<strong>🆕 最近创建：</strong>
<ul>
  {% assign recent_notes = site.notes | sort: "date created" | reverse %}
  {% for note in recent_notes limit: 6 %}
    <li>
      {{ note['date created']}} — <a class="internal-link" href="{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>


<strong>⏰ 最近更新：</strong>

<ul>
  {% assign recent_notes = site.notes | sort: "date modified" | reverse %}
  {% for note in recent_notes limit: 6 %}
    <li>
      {{ note['date modified']}} — <a class="internal-link" href="{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>
