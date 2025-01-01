// 这里可以添加一些前端交互逻辑，比如表单验证等
document.getElementById('login-form').addEventListener('submit', function (event) {
    // 简单的表单验证
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password) {
        alert('用户名和密码不能为空');
        event.preventDefault();
    }
});