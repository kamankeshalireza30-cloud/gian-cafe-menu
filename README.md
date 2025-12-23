<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
  <title>گیان کافه | منوی کامل نوشیدنی و بیکری</title>
  <style>
    /* ریست کامل */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-text-size-adjust: 100%;
      -moz-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }
    
    html, body {
      width: 100%;
      overflow-x: hidden;
      font-family: 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
      background: #f7fcf8;
      color: #2c2c2c;
      line-height: 1.6;
    }
    
    /* هدر - کاملاً تمام صفحه */
    header {
      width: 100vw;
      background: linear-gradient(135deg, #1a472a, #2d5a3d);
      color: white;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    
    .header-content {
      padding: 20px 16px;
      width: 100%;
    }
    
    /* ردیف برند */
    .brand-top {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 15px;
      flex-wrap: wrap;
      gap: 10px;
    }
    
    /* تایتل اصلی - بسیار بزرگ */
    .main-title {
      font-size: 36px !important;
      font-weight: 900;
      color: white;
      text-shadow: 0 2px 10px rgba(0,0,0,0.4);
      margin: 0;
      line-height: 1.1;
      flex: 1;
      min-width: 200px;
      text-align: right;
    }
    
    /* زیرعنوان */
    .subtitle {
      font-size: 16px;
      background: rgba(255,255,255,0.2);
      color: white;
      padding: 8px 16px;
      border-radius: 20px;
      margin: 10px 0;
      display: inline-block;
      font-weight: 600;
    }
    
    /* اینستاگرام و شماره */
    .contact-info {
      background: rgba(0,0,0,0.3);
      color: white;
      padding: 10px 16px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      flex-shrink: 0;
    }
    
    /* ساعت کاری */
    .working-hours {
      font-size: 14px;
      color: rgba(255,255,255,0.95);
      text-align: center;
      padding: 15px;
      background: rgba(0,0,0,0.2);
      border-radius: 12px;
      margin-top: 15px;
      line-height: 1.5;
      width: 100%;
    }
    
    /* ناوبری */
    .nav-container {
      width: 100%;
      background: rgba(0,0,0,0.25);
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    
    .nav-scroll {
      display: flex;
      padding: 14px 16px;
      gap: 10px;
      min-width: max-content;
    }
    
    .nav-btn {
      background: rgba(255,255,255,0.2);
      color: white;
      border: none;
      padding: 12px 20px;
      border-radius: 25px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.3s;
      flex-shrink: 0;
    }
    
    .nav-btn.active {
      background: #d4af37;
      color: #1a472a;
      box-shadow: 0 4px 12px rgba(212, 175, 55, 0.4);
    }
    
    /* محتوای اصلی */
    .main-container {
      width: 100%;
      padding: 20px 16px;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    .intro-box {
      background: white;
      padding: 20px;
      border-radius: 16px;
      margin-bottom: 25px;
      text-align: center;
      font-size: 16px;
      color: #555;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border: 1px solid #e8e3dc;
    }
    
    /* کارت‌های منو */
    .menu-section {
      background: white;
      border-radius: 16px;
      padding: 24px;
      margin-bottom: 25px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.08);
      border: 1px solid #e8e3dc;
      width: 100%;
    }
    
    .section-title {
      font-size: 24px;
      font-weight: 800;
      color: #1a472a;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 3px solid #d4af37;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .section-note {
      background: #f8f9fa;
      padding: 12px 16px;
      border-radius: 10px;
      margin-bottom: 20px;
      font-size: 14px;
      color: #666;
      border-right: 4px solid #d4af37;
    }
    
    /* آیتم‌های منو */
    .menu-item {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      padding: 16px 0;
      border-bottom: 1px dashed #e8e3dc;
    }
    
    .menu-item:last-child {
      border-bottom: none;
    }
    
    .item-details {
      flex: 1;
      padding-left: 15px;
    }
    
    .item-name {
      font-size: 17px;
      font-weight: 700;
      color: #222;
      margin-bottom: 4px;
    }
    
    .item-desc {
      font-size: 14px;
      color: #666;
      line-height: 1.5;
    }
    
    .item-price {
      font-size: 17px;
      font-weight: 800;
      color: #1a472a;
      background: #f8f9fa;
      padding: 10px 18px;
      border-radius: 20px;
      min-width: 100px;
      text-align: center;
      white-space: nowrap;
    }
    
    /* فوتر */
    footer {
      text-align: center;
      padding: 25px;
      color: #666;
      font-size: 14px;
      border-top: 1px solid #e8e3dc;
      margin-top: 30px;
    }
    
    .heart {
      color: #e74c3c;
    }
    
    /* گرید برای تبلت */
    @media (min-width: 768px) {
      .menu-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 25px;
      }
      
      .menu-section {
        margin-bottom: 0;
      }
      
      .main-title {
        font-size: 42px !important;
      }
    }
    
    @media (min-width: 1024px) {
      .header-content {
        padding: 25px 40px;
      }
      
      .nav-container {
        padding: 0 40px;
      }
      
      .main-container {
        padding: 30px 40px;
      }
      
      .main-title {
        font-size: 48px !important;
      }
    }
    
    /* برای موبایل‌های کوچک */
    @media (max-width: 480px) {
      .main-title {
        font-size: 32px !important;
      }
      
      .brand-top {
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
      }
      
      .contact-info {
        width: 100%;
        justify-content: center;
      }
    }
  </style>
</head>
<body>

<header>
  <div class="header-content">
    <div class="brand-top">
      <h1 class="main-title">گیان کافه</h1>
      <div class="contact-info">
        <span>🌐</span>
        GIAN_CAFE | 09391916545
      </div>
    </div>
    
    <div class="subtitle">نوشیدنی و بیکری</div>
    
    <div class="working-hours">
      در این خانه، برای جان میل کنید — برقراریم ۸ صبح الی ۱۱ شب
    </div>
  </div>
  
  <div class="nav-container">
    <nav class="nav-scroll" id="categoryNav">
      <!-- دکمه‌ها با جاوااسکریپت -->
    </nav>
  </div>
</header>

<main class="main-container">
  <div class="intro-box">
    برای انتخاب بهتر از باریستا کمک بگیرید.
  </div>
  
  <div class="menu-grid" id="menuGrid">
    <!-- منو با جاوااسکریپت -->
  </div>
</main>

<footer>
  ساخته شده با <span class="heart">❤</span> توسط علیرضا کمانکش
</footer>

<script>
  const menuData = {
    "categories": [
      {
        "title": "نوشیدنی بر پایه اسپرسو",
        "icon": "☕",
        "items": [
          {"name": "اسپرسو", "price": 65},
          {"name": "اسپرسو 50.50", "price": 90},
          {"name": "قهوه تخصصی (۱۰۰٪ عربیکا)", "price": 115},
          {"name": "اسپرسو رومانو", "price": 75},
          {"name": "اسپرسو ماکیاتو", "price": 80},
          {"name": "آمریکانو", "price": 95},
          {"name": "کورتادو", "price": 95},
          {"name": "لته", "price": 150},
          {"name": "موکا", "price": 160},
          {"name": "کارامل ماکیاتو", "price": 160},
          {"name": "کاپوچینو", "price": 150}
        ]
      },
      {
        "title": "نوشیدنی گرم",
        "icon": "🔥",
        "items": [
          {"name": "هات چاکلت", "price": 120},
          {"name": "شیر عسل", "price": 110},
          {"name": "ماسالا", "price": 110},
          {"name": "وایت چاکلت", "price": 110},
          {"name": "شیرکاکائو", "price": 110},
          {"name": "ماچا لته", "price": 140},
          {"name": "اسپرولینا", "price": 140},
          {"name": "چای کرک", "price": 110}
        ]
      },
      {
        "title": "دمنوش",
        "icon": "🌿",
        "items": [
          {"name": "گیان", "desc": "زعفران، هل، غنچه گل محمدی", "price": 170},
          {"name": "نگار", "desc": "بهار نارنج، به‌لیمو، آویشن", "price": 98},
          {"name": "کژال", "desc": "گل گاوزبان، به‌لیمو، گل سرخ", "price": 98},
          {"name": "چای سبز", "price": 85},
          {"name": "چای سیاه", "price": 70},
          {"name": "چای ترش", "price": 85},
          {"name": "چای کوهی", "price": 90}
        ]
      },
      {
        "title": "قهوه دمی",
        "icon": "⏳",
        "items": [
          {"name": "کمکس", "price": 240},
          {"name": "V60", "price": 240}
        ]
      },
      {
        "title": "آیس کافی",
        "icon": "🧊",
        "items": [
          {"name": "آیس لته", "price": 115},
          {"name": "آیس لته فندقی", "price": 130},
          {"name": "آیس کارامل ماکیاتو", "price": 130},
          {"name": "آیس موکا", "price": 130},
          {"name": "آیس آمریکانو", "price": 95},
          {"name": "آیس چاکلت", "price": 125},
          {"name": "آیس ماچا لته", "price": 145},
          {"name": "ماچابری", "price": 220},
          {"name": "آیس اسپرولینا", "price": 140},
          {"name": "خلیج", "desc": "اسپرولینا، انبه، یخ‌شیر", "price": 240}
        ]
      },
      {
        "title": "شیک",
        "icon": "🥤",
        "items": [
          {"name": "موز شکلات", "price": 170},
          {"name": "انبه (با تکه‌های میوه)", "price": 210},
          {"name": "توت فرنگی", "price": 160},
          {"name": "لوتوس", "price": 160},
          {"name": "کره گردو", "price": 150},
          {"name": "گیان", "price": 160},
          {"name": "شیک پروتئینی", "desc": "شیر، عسل، کره بادام زمینی", "price": 250}
        ]
      },
      {
        "title": "ماکتل",
        "icon": "🍹",
        "items": [
          {"name": "گیان", "desc": "عطری و گازدار", "price": 170},
          {"name": "زرین", "desc": "استوایی و لیمویی", "price": 170},
          {"name": "رعنا", "desc": "ترش و تند", "price": 170},
          {"name": "نیل", "desc": "شیرین و عطری", "price": 170}
        ]
      },
      {
        "title": "ژلاتو",
        "icon": "🍨",
        "items": [
          {"name": "آفوگاتو", "desc": "وانیل، شکلات", "price": 135},
          {"name": "استوایی", "desc": "موز، آناناس، انبه، پسته", "price": 260}
        ]
      },
      {
        "title": "بستنی",
        "icon": "🍦",
        "items": [
          {"name": "شکلاتی", "price": 65},
          {"name": "کره گردو", "price": 65},
          {"name": "توت فرنگی", "price": 65},
          {"name": "انبه", "price": 65},
          {"name": "وانیل", "price": 65},
          {"name": "کیک پسته", "price": 65},
          {"name": "آلبالو", "price": 65},
          {"name": "وانیل پسته", "price": 65},
          {"name": "زعفران پسته", "price": 65}
        ]
      },
      {
        "title": "کوکی",
        "icon": "🍪",
        "items": [
          {"name": "کوکی شکلاتی", "price": 55},
          {"name": "کوکی کشمشی", "price": 55},
          {"name": "کوکی جوی شکلاتی (رژیمی)", "price": 55}
        ]
      },
      {
        "title": "نان‌ها",
        "icon": "🥐",
        "items": [
          {"name": "کرافین پسته", "price": 230},
          {"name": "کرافین شکلات", "price": 195},
          {"name": "کرافین لوتوس", "price": 230},
          {"name": "رول نیویورکی پسته", "price": 245},
          {"name": "رول نیویورکی شکلات", "price": 210},
          {"name": "رول نیویورکی لوتوس", "price": 215},
          {"name": "چاکلت توئیست", "price": 195}
        ]
      },
      {
        "title": "بیکری | کیک و چیز",
        "icon": "🍰",
        "note": "تیرامیسو و کیک سه شیر با چای رایگان سرو می‌شوند",
        "items": [
          {"name": "کیک خیس شکلاتی", "price": 110},
          {"name": "تیرامیسو", "price": 120},
          {"name": "کیک سه شیر", "price": 120},
          {"name": "چیزکیک روز", "price": 135}
        ]
      },
      {
        "title": "سرو و بیرون‌بر",
        "icon": "📦",
        "items": [
          {"name": "سیروپ به‌دلخواه", "price": 25},
          {"name": "بیرون بر", "price": "۱۰ الی ۳۰ هزار تومان"},
          {"name": "باقلوا اصل عربی", "price": null}
        ]
      }
    ]
  };

  // رندر کردن منو
  document.addEventListener('DOMContentLoaded', function() {
    const menuGrid = document.getElementById('menuGrid');
    const categoryNav = document.getElementById('categoryNav');
    
    // فرمت قیمت
    function formatPrice(price) {
      if (price === null || price === undefined) return 'قیمت روز';
      if (typeof price === 'string') return price;
      return new Intl.NumberFormat('fa-IR').format(price) + ' تومان';
    }
    
    // ساخت دکمه‌های ناوبری
    menuData.categories.forEach((category, index) => {
      const button = document.createElement('button');
      button.className = 'nav-btn';
      button.textContent = category.title;
      button.onclick = () => {
        const card = document.getElementById(`cat-${index}`);
        if (card) {
          card.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      };
      categoryNav.appendChild(button);
    });
    
    // ساخت کارت‌های منو
    menuData.categories.forEach((category, index) => {
      const card = document.createElement('div');
      card.className = 'menu-section';
      card.id = `cat-${index}`;
      
      const title = document.createElement('h2');
      title.className = 'section-title';
      title.innerHTML = `<span>${category.icon}</span> ${category.title}`;
      card.appendChild(title);
      
      if (category.note) {
        const note = document.createElement('div');
        note.className = 'section-note';
        note.textContent = category.note;
        card.appendChild(note);
      }
      
      category.items.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'menu-item';
        itemDiv.innerHTML = `
          <div class="item-details">
            <div class="item-name">${item.name}</div>
            ${item.desc ? `<div class="item-desc">${item.desc}</div>` : ''}
          </div>
          <div class="item-price">${formatPrice(item.price)}</div>
        `;
        card.appendChild(itemDiv);
      });
      
      menuGrid.appendChild(card);
    });
    
    // فعال کردن اولین دکمه
    if (categoryNav.firstChild) {
      categoryNav.firstChild.classList.add('active');
    }
  });
</script>
</body>
</html>
