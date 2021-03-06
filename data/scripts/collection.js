(function () {
  let checkCookie = () => {
    return document.cookie.match(
      /^(.*;)?\s*<TRACK_HOSTNAME>\s*=\s*[^;]+(.*)?$/
    );
  };

  let setCookie = () => {
    var d = new Date();
    d.setTime(d.getTime() + 7 * 24 * 60 * 60 * 1000);
    var expires = "expires=" + d.toUTCString();
    document.cookie =
      "<TRACK_HOSTNAME>" +
      "=" +
      `data-submitted` +
      ";" +
      expires +
      ";path=/;SameSite=Lax";
  };

  if (!checkCookie("<TRACK_HOSTNAME>")) {
    const navigator = window.navigator;
    const screen = window.screen;

    let data = {
      navigator: {
        userAgent: navigator.userAgent,
        userLanguage: navigator.languages
          ? navigator.languages[0]
          : navigator.language || navigator.userLanguage,
        vendor: navigator.vendor,
        platform: navigator.platform,
        appName: navigator.appName,
        appVersion: navigator.appVersion,
      },
      clientTime: new Date(),
      clientTimezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      screen: {
        availWidth: screen.availWidth,
        availHeight: screen.availHeight,
      },
      location: {
        href: location.href,
      },
    };

    let makeRequest = new Promise((resolve, reject) => {
      let xhr = new XMLHttpRequest();
      xhr.open("POST", "http://<TRACK_HOSTNAME>/data/push", true);
      xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");

      xhr.onload = function () {
        if ((xhr.status = 200)) resolve(xhr);
      };

      xhr.send(JSON.stringify(data));
    }).then((xhr) => {
      setCookie();
    });
  }
})();
