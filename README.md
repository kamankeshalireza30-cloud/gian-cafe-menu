<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1,user-scalable=no">
  <title>گیان کافه | منوی کامل نوشیدنی و بیکری</title>
  <style>
    /* متغیرهای رنگ */
    :root {
      --primary: #1a472a; /* سبز تیره حرفه‌ای */
      --secondary: #d4af37; /* طلایی */
      --light: #f7fcf8; /* بک‌گراند روشن */
      --dark: #2c2c2c; /* متن تیره */
      --gray: #6c757d; /* متن خاکستری */
      --white: #f9fcfa;
      --shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      --radius: 12px;
      --transition: all 0.3s ease;
    }

    /* ریست استایل‌ها */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
      background-color: var(--light);
      color: var(--dark);
      line-height: 1.6;
      padding-bottom: 40px;
    }

    /* هدر - کاملاً ریسپانسیو */
    .header {
      background: linear-gradient(135deg, var(--primary), #2d5a3d);
      color: var(--white);
      padding: 0;
      box-shadow: var(--shadow);
      position: sticky;
      top: 0;
      z-index: 100;
      width: 100%;
      overflow: hidden;
    }

    .brand-container {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 12px;
      width:100% ;
    }

    .brand-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      gap: 10px;
    }

    .brand-title {
      font-size: 28px !important;
      font-weight: 900;
      letter-spacing: -0.5px;
      line-height: 1.2;
      margin: 0;
      color:#ffffff;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.03);
      width: 100%;
      display: block;
    }

    .brand-subtitle {
      font-size: 14px;
      color: #ffffff;
      background: rgba(255, 255, 255, 0.25);
      padding: 6px 12px;
      border-radius: 20px;
     margin-top: 8px;
     display: inline-block;
     font-weight: 600;
     backdrop-filter: blur(10px);
    }

    .brand-instagram {
      font-size: 13px;
      color:#ffffff;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      background: rgba(0, 0, 0, 0.03);
      padding: 8px 14px;
      border-radius: 20px;
      font-weight: 600;
      flex-shrink: 0;
    }

    .hours {
      font-size: 13px;
      color: rgba(255, 255, 255, 0.95);
      text-align: center;
      padding-top: 12px 0;
      border-top: 2px solid rgba(255, 255, 255, 0.2);
      margin-top: 12px;
      
    }

    /* ناوبری دسته‌ها */
    .categories-nav {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 10px 0;
      margin-top: 10px;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }

    .categories-nav::-webkit-scrollbar {
      display: none;
    }

    .category-btn {
      background: rgba(255, 255, 255, 0.15);
      border: none;
      color: var(--white);
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 500;
      white-space: nowrap;
      cursor: pointer;
      transition: var(--transition);
    }

    .category-btn.active,
    .category-btn:hover {
      background: var(--secondary);
      color: var(--primary);
      font-weight: 600;
    }

    /* محتوای اصلی */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px 16px;
    }

    /* کارت منو */
    .menu-section {
      background: var(--white);
      border-radius: var(--radius);
      padding: 22px;
      margin-bottom: 24px;
      box-shadow: var(--shadow);
      border: 1px solid rgba(0, 0, 0, 0.05);
    }

    .section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--light);
    }

    .section-title {
      font-size: 22px;
      font-weight: 700;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .section-icon {
      color: var(--secondary);
      font-size: 20px;
    }

    .section-note {
      font-size: 13px;
      color: var(--gray);
      background: #f8f9fa;
      padding: 8px 12px;
      border-radius: 8px;
      margin-top: -10px;
      margin-bottom: 15px;
      border-right: 3px solid var(--secondary);
    }

    /* آیتم‌های منو */
    .menu-item {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      padding: 14px 0;
      border-bottom: 1px dashed #e9ecef;
      transition: var(--transition);
    }

    .menu-item:last-child {
      border-bottom: none;
    }

    .menu-item:hover {
      background: #fafafa;
      padding: 14px 10px;
      border-radius: 8px;
      margin: 0 -10px;
    }

    .item-info {
      flex: 1;
      padding-left: 15px;
    }

    .item-name {
      font-size: 16px;
      font-weight: 600;
      color: var(--dark);
      margin-bottom: 4px;
    }

    .item-desc {
      font-size: 13px;
      color: var(--gray);
      line-height: 1.5;
    }

    .item-price {
      font-size: 17px;
      font-weight: 700;
      color: var(--primary);
      background: #f8f9fa;
      padding: 8px 16px;
      border-radius: 20px;
      min-width: 90px;
      text-align: center;
      white-space: nowrap;
    }

    /* فوتر */
    .footer {
      text-align: center;
      padding: 25px 16px;
      color: var(--gray);
      font-size: 13px;
      border-top: 1px solid #e9ecef;
      margin-top: 30px;
    }

    .heart {
      color: #e74c3c;
      margin: 0 5px;
    }

    /* منوی معرفی */
    .menu-intro {
      background: var(--white);
      border-radius: var(--radius);
      padding: 16px;
      margin-bottom: 20px;
      text-align: center;
      font-size: 15px;
      color: var(--gray);
      box-shadow: var(--shadow);
      border: 1px solid rgba(0, 0, 0, 0.05);
    }

    /* حالت پرینت */
    @media print {
      .header,
      .categories-nav,
      .footer,
      .menu-intro {
        display: none;
      }
      
      .menu-section {
        box-shadow: none;
        border: 1px solid #ddd;
        page-break-inside: avoid;
      }
    }

    /* رسپانسیو برای تبلت */
    @media (min-width: 768px) {
      .header {
        padding: 20px 30px;
      }
      
      .container {
        padding: 25px 30px;
      }
      
      .brand-title {
        font-size: 32px;
      }
      
      .brand-row {
        flex-wrap: nowrap;
      }
      
      .categories-nav {
        justify-content: center;
        gap: 12px;
      }
      
      .category-btn {
        padding: 10px 20px;
        font-size: 14px;
      }
      
      .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 25px;
      }
      
      .menu-section {
        margin-bottom: 0;
      }
      
      .menu-intro {
        font-size: 16px;
        padding: 18px;
      }
    }

    /* رسپانسیو برای دسکتاپ */
    @media (min-width: 1024px) {
      .container {
        padding: 30px 40px;
      }
      
      .brand-title {
        font-size: 36px;
      }
      
      .brand-container {
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
      }
      
      .hours {
        text-align: right;
        border-top: none;
        padding-top: 0;
        margin-top: 0;
        border-right: 1px solid rgba(255, 255, 255, 0.15);
        padding-right: 15px;
      }
      
      .menu-grid {
        grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      }
    }

    /* برای موبایل‌های خیلی کوچک */
    @media (max-width: 360px) {
      .brand-title {
        font-size: 24px;
      }
      
      .section-title {
        font-size: 20px;
      }
      
      .item-price {
        font-size: 15px;
        min-width: 80px;
        padding: 6px 12px;
      }
    }
  </style>
</head>
<body>

<header class="header">
  <div class="brand-container">
    <div class="brand-row">
      <div>
        <h1 class="brand-title">گیان کافه</h1>
        <div class="brand-subtitle">نوشیدنی و بیکری</div>
      </div>
      <div class="brand-instagram">
        <span>🌐</span>
        GIAN_CAFE
       ,,,
        09391916545
      </div>
    </div>
    <div class="hours">
      در این خانه، برای جان میل کنید — برقراریم ۸ صبح الی ۱۱ شب
    </div>
  </div>
  
  <nav class="categories-nav" id="categoriesNav">
    <!-- دکمه‌های دسته‌بندی با جاوااسکریپت پر می‌شوند -->
  </nav>
</header>

<main class="container">
  <div class="menu-intro">
    <p>برای انتخاب بهتر از باریستا کمک بگیرید.</p>
  </div>
  
  <div class="menu-grid" id="menuGrid">
    <!-- منو با جاوااسکریپت پر می‌شود -->
  </div>
</main>

<footer class="footer">
  <p>ساخته شده با <span class="heart">❤</span> توسط علیرضا کمانکش</p>
</footer>

<script id="menu-data" type="application/json">
{
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
}
</script>

<script>
  // مقداردهی اولیه
  const menuData = JSON.parse(document.getElementById('menu-data').textContent);
  const menuGrid = document.getElementById('menuGrid');
  const categoriesNav = document.getElementById('categoriesNav');
  let activeCategory = 0;

  // فرمت کردن قیمت
  function formatPrice(price) {
    if (price === null || price === undefined) return 'قیمت روز';
    if (typeof price === 'string') return price;
    return new Intl.NumberFormat('fa-IR').format(price) + ' تومان';
  }

  // ساخت کارت یک دسته‌بندی
  function createCategoryCard(category, index) {
    const card = document.createElement('div');
    card.className = 'menu-section';
    card.id = `category-${index}`;
    
    // هدر دسته‌بندی
    const header = document.createElement('div');
    header.className = 'section-header';
    header.innerHTML = `
      <h2 class="section-title">
        <span class="section-icon">${category.icon}</span>
        ${category.title}
      </h2>
    `;
    card.appendChild(header);
    
    // یادداشت (اگر وجود دارد)
    if (category.note) {
      const note = document.createElement('div');
      note.className = 'section-note';
      note.textContent = category.note;
      card.appendChild(note);
    }
    
    // آیتم‌ها
    category.items.forEach(item => {
      const itemElement = document.createElement('div');
      itemElement.className = 'menu-item';
      itemElement.innerHTML = `
        <div class="item-info">
          <div class="item-name">${item.name}</div>
          ${item.desc ? `<div class="item-desc">${item.desc}</div>` : ''}
        </div>
        <div class="item-price">
          ${formatPrice(item.price)}
        </div>
      `;
      card.appendChild(itemElement);
    });
    
    return card;
  }

  // ساخت دکمه‌های ناوبری
  function createCategoryButtons() {
    menuData.categories.forEach((category, index) => {
      const button = document.createElement('button');
      button.className = `category-btn ${index === 0 ? 'active' : ''}`;
      button.textContent = category.title;
      button.dataset.index = index;
      
      button.addEventListener('click', () => {
        // حذف کلاس active از همه دکمه‌ها
        document.querySelectorAll('.category-btn').forEach(btn => {
          btn.classList.remove('active');
        });
        
        // اضافه کردن active به دکمه کلیک شده
        button.classList.add('active');
        activeCategory = index;
        
        // اسکرول به بخش مربوطه
        const targetCard = document.getElementById(`category-${index}`);
        if (targetCard) {
          window.scrollTo({
            top: targetCard.offsetTop - 100,
            behavior: 'smooth'
          });
        }
      });
      
      categoriesNav.appendChild(button);
    });
  }

  // رندر کردن منو
  function renderMenu() {
    menuGrid.innerHTML = '';
    categoriesNav.innerHTML = '';
    
    // ایجاد دکمه‌های ناوبری
    createCategoryButtons();
    
    // ایجاد کارت‌های دسته‌بندی
    menuData.categories.forEach((category, index) => {
      const card = createCategoryCard(category, index);
      menuGrid.appendChild(card);
    });
  }

  // فعال کردن خودکار دکمه هنگام اسکرول
  function handleScroll() {
    const cards = document.querySelectorAll('.menu-section');
    const navButtons = document.querySelectorAll('.category-btn');
    
    let currentIndex = -1;
    
    cards.forEach((card, index) => {
      const rect = card.getBoundingClientRect();
      if (rect.top <= 150 && rect.bottom >= 150) {
        currentIndex = index;
      }
    });
    
    if (currentIndex >= 0 && currentIndex !== activeCategory) {
      navButtons.forEach(btn => btn.classList.remove('active'));
      navButtons[currentIndex]?.classList.add('active');
      activeCategory = currentIndex;
    }
  }

  // مقداردهی اولیه
  document.addEventListener('DOMContentLoaded', () => {
    renderMenu();
    window.addEventListener('scroll', handleScroll);
    
    // اضافه کردن event listener برای ریسایز پنجره
    window.addEventListener('resize', () => {
      // بهینه‌سازی نمایش در سایزهای مختلف
    });
  });
</script>
</body>
</html>
