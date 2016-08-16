---
layout: post
title: "AMY bugfix release v1.7.2"
tags: [swcarpentry, django, release notes]
date: 2016-08-16
---

AMY [v1.7.2][] was released today. It contains one bug fix provided by
[Aditya Narayan][].

Aditya fixed a bug throwing 500 HTTP error when accessing
`/api/v1/todos/user/`.  This API endpoint is being accessed by the browser
whenever any admin user loads their dashboard.

  [v1.7.2]: https://github.com/swcarpentry/amy/milestone/34
  [Aditya Narayan]: https://github.com/narayanaditya95
