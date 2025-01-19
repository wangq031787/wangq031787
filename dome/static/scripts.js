// 这里可以添加一些前端交互逻辑，比如轮播图、点击事件等
document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('DOMContentLoaded', function () {
        // 示例：轮播图逻辑
        const bannerRight = document.querySelector('.banner_right');
        const images = bannerRight.querySelectorAll('img');

        // 在 scripts.js 中引用图片
        const imgElement = document.createElement('img');
        imgElement.src = '/static/images/hd.jpg';
        document.body.appendChild(imgElement);
        let currentIndex = 0;

        function showImage(index) {
            images.forEach((img, i) => {
                img.style.display = i === index ? 'block' : 'none';
            });
        }

        function nextImage() {
            currentIndex = (currentIndex + 1) % images.length;
            showImage(currentIndex);
        }

        function prevImage() {
            currentIndex = (currentIndex - 1 + images.length) % images.length;
            showImage(currentIndex);
        }

        document.querySelector('.zuo').addEventListener('click', prevImage);
        document.querySelector('.you').addEventListener('click', nextImage);

        // 初始化显示第一张图片
        showImage(currentIndex);

    });
