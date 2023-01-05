document.addEventListener(
  "DOMContentLoaded",
  () => {
    Array.from(document.getElementsByClassName("showsimilar")).forEach(
      (el) => {
        let input = el.previousElementSibling;
        ["keyup", "cut", "paste", "onchange"].forEach((ev) => {
          input.addEventListener(ev, () => timer(input));
        });
      }
    );

    function timer(el) {
      clearTimeout(el.dataset.showsimilar_timer);
      el.dataset.showsimilar_timer = setTimeout(() => { search(el) }, 600);
    };

    function search(el) {
      let url = new URL(
        window.location.protocol+ window.location.host +
        "/admin/showsimilar/search/"
      );
      url.searchParams.set("query", el.value);
      url.searchParams.set("field", el.getAttribute("name"));

      let items_div = el.nextElementSibling;

      url.searchParams.set("model", items_div.dataset.model);
      url.searchParams.set("instance_id", items_div.dataset.id);
      url.searchParams.set("threshold", items_div.dataset.threshold);
      url.searchParams.set("max_items", items_div.dataset.max_items);

      fetch(url)
        .then(response => response.json())
        .then(data => {
          items_div.innerText = "";

          if (data.items.length) {
            let label = items_div.appendChild(document.createElement("span"));
            label.textContent = items_div.dataset.label;

            let items_ul = items_div.appendChild(document.createElement("ul"));
            data.items.forEach(d => {
              let li = items_ul.appendChild(document.createElement("li"));
              if (d.url === null) {
                li.innerText = d.value;
              } else {
                let item = li.appendChild(document.createElement("a"));
                item.href = d.url;
                item.target = "_blank";
                item.textContent = d.value;
              }
            });
            if (data.is_trimmed) {
              let li = items_ul.appendChild(document.createElement("li"));
              li.innerText = "...";
            }
          }
        });
    };
  }
);
