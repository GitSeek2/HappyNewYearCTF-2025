# Apache PHP

此目录用于构建低版本（<5.4） PHP 镜像。

官方镜像 [php:5.3.29-apache](https://hub.docker.com/layers/library/php/5.3.29-apache/images/sha256-f2c7c150fd7941a90f9b95777f1af5932ec51babe66f85c0860fea34c042d119) 已不可用[^1]。

基础镜像：

- **kuborgh/php-5.2**：[GitHub](https://github.com/kuborgh/docker-php-5.2), [Docker Hub](https://hub.docker.com/r/kuborgh/php-5.2)
- **eugeneware/php-5.3**：[GitHub](https://github.com/eugeneware/docker-php-5.3-apache), [Docker Hub](https://hub.docker.com/r/eugeneware/php-5.3)

eugeneware/php-5.3 可能参考了 [Drop php 5.3 by yosifkit · Pull Request #20 · docker-library/php](https://github.com/docker-library/php/pull/20#issuecomment-120163754) 提到的 [个人方案](https://hub.docker.com/u/helder/?page=1&search=php)。

[^1]: [Deprecated Docker Engine features | Pushing and pulling with image manifest v2 schema 1](https://docs.docker.com/engine/deprecated/#pushing-and-pulling-with-image-manifest-v2-schema-1)
