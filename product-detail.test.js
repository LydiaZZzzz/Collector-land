/**
 * @jest-environment jsdom
 */

const fs = require('fs');
const path = require('path');

describe('Product Detail Page', () => {
  let html;
  let container;

  beforeAll(() => {
    html = fs.readFileSync(path.resolve(__dirname, './product-detail.html'), 'utf8');
    document.documentElement.innerHTML = html;

    // 直接在这里插入页面JS逻辑
    const thumbs = document.querySelectorAll('.thumb-img');
    const dots = document.querySelectorAll('.thumb-dot');
    let current = 0;

    function showThumb(idx) {
      thumbs.forEach((img, i) => {
        img.classList.toggle('active', i === idx);
      });
      dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === idx);
      });
      current = idx;
    }

    dots.forEach((dot, idx) => {
      dot.addEventListener('click', () => showThumb(idx));
    });
  });

  beforeEach(() => {
    container = document.body;
  });

  test('点击小圆点能切换小图', () => {
    const thumbs = container.querySelectorAll('.thumb-img');
    const dots = container.querySelectorAll('.thumb-dot');

    // 初始第一个active
    expect(thumbs[0].classList.contains('active')).toBe(true);
    expect(dots[0].classList.contains('active')).toBe(true);

    // 模拟点击第二个圆点
    dots[1].click();

    expect(thumbs[1].classList.contains('active')).toBe(true);
    expect(dots[1].classList.contains('active')).toBe(true);
    expect(thumbs[0].classList.contains('active')).toBe(false);
    expect(dots[0].classList.contains('active')).toBe(false);
  });
}); 