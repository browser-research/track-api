(function () {
  const navigator = window.navigator;
  const screen = window.screen;

  let data = {
    navigator: {
      userAgent: navigator.userAgent,
      userLanguage: navigator.userLanguage,
      vendor: navigator.vendor,
      language: navigator.language,
      platform: navigator.platform,
      appName: navigator.appName,
      appVersion: navigator.appVersion,
    },
    screen: {
      availWidth: screen.availWidth,
      availHeight: screen.availHeight,
    },
    location: {
      href: location.href,
    },
  };

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "http://<API_HOSTNAME>/data/push", true);
  xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
  xhr.send(JSON.stringify(data));
})();
