"""
generate_pages.py
Generates all inner HTML pages for the Jackson Osborne site.
Run once: python3 generate_pages.py
"""

import os

# ── SHARED LOGO SVG ──────────────────────────────────────────────────────────
LOGO_SVG = """      <svg viewBox="0 0 72 72" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="lg1" x1="0" y1="0" x2="72" y2="72" gradientUnits="userSpaceOnUse">
            <stop offset="0%"   stop-color="#289dcc"/>
            <stop offset="60%"  stop-color="#0087ba"/>
            <stop offset="100%" stop-color="#006a93"/>
          </linearGradient>
        </defs>
        <rect x="1" y="1" width="70" height="70" rx="7" fill="url(#lg1)"/>
        <rect x="1" y="1" width="70" height="20" rx="7" fill="rgba(255,255,255,0.06)"/>
        <ellipse cx="42" cy="38" rx="17" ry="21" stroke="white" stroke-width="3.0" fill="none" opacity="0.88" transform="rotate(-4 42 38)"/>
        <path d="M31 13 C31.5 13 32 13.2 32 14 L32 49 C32 53 29.5 57.5 25 59 C20.5 60.5 16.5 58 15.5 54.5 C14.8 52 15.8 49.5 17.5 48.2" stroke="white" stroke-width="3.6" stroke-linecap="round" fill="none"/>
        <path d="M23 13 C25 12.5 28 12.5 32 13 C35.5 13.5 38 13.5 39.5 13" stroke="white" stroke-width="2.4" stroke-linecap="round" fill="none"/>
      </svg>"""

def header(root):
    """root = '../' for subfolders, '' for root-level pages"""
    return f"""<header id="header">
  <div class="hdr">
    <a href="{root}index.html" class="logo">
{LOGO_SVG}
      <div class="logo-txt">
        <span class="logo-name">Jackson</span>
        <span class="logo-name logo-grey">Osborne</span>
        <span class="logo-sub">employment lawyers</span>
      </div>
    </a>
    <nav>
      <div class="nd">
        <a href="{root}employers/index.html" class="nl">For Employers</a>
        <div class="dm">
          <a href="{root}employers/tribunal.html">Tribunal &amp; Court Representation</a>
          <a href="{root}employers/settlement.html">Settlement Agreements</a>
          <a href="{root}employers/disciplinary.html">Disciplinary &amp; Investigations</a>
          <a href="{root}employers/contracts.html">Contracts &amp; Policies</a>
          <a href="{root}employers/directors.html">Directors' Service Agreements</a>
          <a href="{root}employers/redundancy.html">Redundancy</a>
          <a href="{root}employers/restrictive-covenants.html">Restrictive Covenants</a>
          <a href="{root}employers/discrimination.html">Discrimination &amp; Harassment</a>
          <a href="{root}employers/tupe.html">TUPE &amp; Business Acquisitions</a>
        </div>
      </div>
      <div class="nd">
        <a href="{root}employees/index.html" class="nl">For Employees</a>
        <div class="dm">
          <a href="{root}employees/unfair-dismissal.html">Unfair &amp; Constructive Dismissal</a>
          <a href="{root}employees/settlement.html">Settlement Agreements</a>
          <a href="{root}employees/discrimination.html">Discrimination &amp; Harassment</a>
          <a href="{root}employees/whistleblowing.html">Whistleblowing</a>
          <a href="{root}employees/restrictive-covenants.html">Restrictive Covenants</a>
        </div>
      </div>
      <a href="{root}monthly-retainer.html" class="nl">Monthly Retainer</a>
      <a href="{root}freedom-rights.html"   class="nl">Freedom Rights</a>
      <a href="{root}news/index.html"       class="nl">Updates</a>
      <a href="{root}charges.html"          class="nl">Charges</a>
      <a href="{root}contact.html"          class="nl ncta">Get Advice</a>
    </nav>
    <button class="mob-menu" id="mob-open" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div id="mob" class="mob-overlay">
  <button class="mob-close" id="mob-close">&#x2715;</button>
  <a href="{root}index.html"                             class="mob-nav-link">Home</a>
  <p class="mob-section-title">For Employers</p>
  <a href="{root}employers/index.html"                   class="mob-sub-link">Overview</a>
  <a href="{root}employers/tribunal.html"                class="mob-sub-link">Tribunal &amp; Court</a>
  <a href="{root}employers/disciplinary.html"            class="mob-sub-link">Disciplinary &amp; Investigations</a>
  <a href="{root}employers/contracts.html"               class="mob-sub-link">Contracts &amp; Policies</a>
  <a href="{root}employers/redundancy.html"              class="mob-sub-link">Redundancy</a>
  <a href="{root}employers/restrictive-covenants.html"   class="mob-sub-link">Restrictive Covenants</a>
  <a href="{root}employers/tupe.html"                    class="mob-sub-link">TUPE</a>
  <p class="mob-section-title">For Employees</p>
  <a href="{root}employees/index.html"                   class="mob-sub-link">Overview</a>
  <a href="{root}employees/unfair-dismissal.html"        class="mob-sub-link">Unfair Dismissal</a>
  <a href="{root}employees/settlement.html"              class="mob-sub-link">Settlement Agreements</a>
  <a href="{root}employees/discrimination.html"          class="mob-sub-link">Discrimination</a>
  <a href="{root}employees/whistleblowing.html"          class="mob-sub-link">Whistleblowing</a>
  <a href="{root}monthly-retainer.html" class="mob-nav-link">Monthly Retainer</a>
  <a href="{root}freedom-rights.html"   class="mob-nav-link">Freedom Rights</a>
  <a href="{root}news/index.html"       class="mob-nav-link">News &amp; Updates</a>
  <a href="{root}charges.html"          class="mob-nav-link">Our Charges</a>
  <a href="{root}contact.html"          class="mob-nav-link">Contact Us</a>
</div>"""

def footer(root):
    return f"""<footer>
  <div class="fin">
    <div class="ftop">
      <div class="fbrand">
        <div class="flogo">Jackson Osborne</div>
        <div class="ftag2">Employment Lawyers</div>
        <p>A niche employment law firm founded in 2010, providing expert representation and advice to employers, senior executives, and individuals across Wales and England.</p>
      </div>
      <div class="fc">
        <h4>For Employers</h4>
        <a href="{root}employers/tribunal.html">Tribunal Representation</a>
        <a href="{root}employers/disciplinary.html">Disciplinary &amp; Grievance</a>
        <a href="{root}employers/redundancy.html">Redundancy</a>
        <a href="{root}employers/restrictive-covenants.html">Restrictive Covenants</a>
        <a href="{root}employers/tupe.html">TUPE</a>
        <a href="{root}monthly-retainer.html">Monthly Retainer</a>
      </div>
      <div class="fc">
        <h4>For Employees</h4>
        <a href="{root}employees/unfair-dismissal.html">Unfair Dismissal</a>
        <a href="{root}employees/settlement.html">Settlement Agreements</a>
        <a href="{root}employees/discrimination.html">Discrimination</a>
        <a href="{root}employees/whistleblowing.html">Whistleblowing</a>
        <a href="{root}employees/restrictive-covenants.html">Restrictive Covenants</a>
      </div>
      <div class="fc">
        <h4>The Firm</h4>
        <a href="{root}news/index.html">News &amp; Know-how</a>
        <a href="{root}charges.html">Our Charges</a>
        <a href="{root}freedom-rights.html">Freedom Rights</a>
        <a href="{root}contact.html">Contact Us</a>
      </div>
    </div>
    <div class="fbot">
      <span>&copy; 2026 Jackson Osborne. All rights reserved. Authorised and regulated by the SRA.</span>
      <span><a href="{root}privacy.html">Privacy</a><a href="{root}complaints.html">Complaints</a></span>
    </div>
  </div>
</footer>"""

def page_hero(breadcrumb_html, title_html, subtitle):
    return f"""<div class="page-top">
  <div class="page-hero">
    <div class="page-hero-bg"></div>
    <div class="page-hero-grid"></div>
    <div class="page-hero-body">
      <div class="page-breadcrumb">{breadcrumb_html}</div>
      <h1 class="page-title">{title_html}</h1>
      <p class="page-sub">{subtitle}</p>
    </div>
  </div>
</div>"""

def build(filepath, title, css_root, js_root, head_root, body_content):
    """Write a complete HTML file."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Jackson Osborne Employment Lawyers</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_root}css/style.css">
</head>
<body>

{header(head_root)}

{body_content}

{footer(head_root)}

<script src="{js_root}js/main.js"></script>
</body>
</html>"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(html)
    print(f"  ✓  {filepath}")

BASE = "/home/claude/jo-site"

# ── ROOT = '' (pages in root folder) ────────────────────────────────────────

# monthly-retainer.html
build(f"{BASE}/monthly-retainer.html",
  "Monthly Retainer", "", "", "",
  page_hero(
    '<a href="index.html">Home</a> <span>→ Monthly Retainer</span>',
    "Fixed Monthly <em>Retainer</em>",
    "Expert employment law protection for your business on a fixed, predictable monthly cost."
  ) + """
<section class="ret" style="padding-top:80px">
  <div class="ret-in">
    <div>
      <div class="ret-lbl">Employment Support Retainer</div>
      <h2 class="ret-title">Protection from experts.<br><em>Priced for the real world.</em></h2>
      <p class="ret-desc">We offer an Employment Support Retainer on a fixed cost monthly basis to help your business avoid claims — and defend those that cannot be avoided. We give you a health check, update your contracts and policies, and provide ongoing expert advice from experienced, qualified professionals.</p>
      <div class="ret-price">
        <div class="ret-price-lbl">From as little as</div>
        <div class="ret-price-val">£1 per employee / week <small>or £100/month</small></div>
      </div>
      <ul class="ret-features">
        <li><span class="fdot"></span>Contracts &amp; policies health check on commencement</li>
        <li><span class="fdot"></span>Unlimited access to senior, qualified solicitors — not juniors</li>
        <li><span class="fdot"></span>Full tribunal defence support at no additional cost</li>
        <li><span class="fdot"></span>Insurance available covering legal costs and compensation awards</li>
        <li><span class="fdot"></span>No "reasonable prospects" clause — follow our advice and you are covered</li>
        <li><span class="fdot"></span>Tailored cost depending on headcount, sector, and risk profile</li>
      </ul>
      <br><a href="contact.html" class="btn-p">Discuss a Retainer →</a>
    </div>
    <div class="ret-box">
      <p class="ret-q">"Direct and to the point. Jackson Osborne have saved us many thousands of pounds in dealing with issues that other providers were afraid of and didn't have the skill to tackle."</p>
      <p class="ret-qa">Robert Humphries — Managing Director, B.A.S. International</p>
      <div class="ret-bens">
        <div class="ret-ben"><div class="ret-ben-n">£102k+</div><div class="ret-ben-l">Maximum unfair dismissal award now in force</div></div>
        <div class="ret-ben"><div class="ret-ben-n">1/5min</div><div class="ret-ben-l">New ET claim issued since fee abolition</div></div>
        <div class="ret-ben"><div class="ret-ben-n">£2–5k</div><div class="ret-ben-l">Per day legal defence costs at tribunal</div></div>
        <div class="ret-ben"><div class="ret-ben-n">No cap</div><div class="ret-ben-l">On discrimination &amp; whistleblowing awards</div></div>
      </div>
    </div>
  </div>
</section>
<section class="sec"><div class="sec-inner">
  <h2 class="sec-title">Why our retainer <em>is different.</em></h2>
  <div class="prose">
    <p>You may have experience of telephone helplines where the adviser is junior, unqualified and inexperienced. Even if you get to speak to a team manager, the advice is "no, you can't do that" — and you are no further forward.</p>
    <p>You won't find that with us. Our objective is to help you exercise your employer's rights and run your business effectively. If an employee still wants to make a claim, we support and represent you all the way to full defence at trial — without further cost to your balance sheet.</p>
    <h3>Insurance backing</h3>
    <p>Insurance is available to cover legal costs and compensation awards in the event of any claim. There is no "reasonable prospects" clause. The basic principle: if you follow our advice, you will be covered.</p>
  </div>
</div></section>""")

# charges.html
build(f"{BASE}/charges.html",
  "Our Charges", "", "", "",
  page_hero(
    '<a href="index.html">Home</a> <span>→ Our Charges</span>',
    "Our <em>Charges</em>",
    "Transparent, competitive pricing — consistently 35–45% less than comparable City practices."
  ) + """
<section class="sec"><div class="sec-inner">
  <div class="two-col-3">
    <div>
      <div class="sec-lbl">Pricing Approach</div>
      <h2 class="sec-title">Fair fees. <em>Outstanding value.</em></h2>
      <div class="prose">
        <p>Our partner and senior solicitor hourly rates are consistently 35–45% less than solicitors with equivalent experience in large commercial practices. We face such practices in disputes regularly — and come out winning.</p>
        <h3>Hourly rates</h3>
        <p>Our hourly rates for partner and senior solicitor work are typically in the range of £180–£280 plus VAT, depending on the complexity of the matter. We will always give you a clear indication of likely costs at the outset.</p>
        <h3>Fixed fees</h3>
        <p>For many matters we offer fixed fees — particularly for document drafting, settlement agreement review, and defined advisory projects. This gives you cost certainty from the outset.</p>
        <h3>Monthly Retainer</h3>
        <p>For employers, our Monthly Retainer provides fixed-cost access to senior employment law advice from as little as £1 per employee per week or £100 per month.</p>
        <h3>Conditional arrangements</h3>
        <p>In appropriate cases, particularly for employee claimants, we are able to discuss conditional fee arrangements. Please contact us to discuss.</p>
      </div>
      <a href="contact.html" class="btn-blue" style="margin-top:24px">Discuss Our Fees →</a>
    </div>
    <div>
      <div class="stat-row" style="grid-template-columns:1fr 1fr;margin-top:0">
        <div class="stat-box"><div class="stat-box-num">35–45%</div><div class="stat-box-lbl">Less than City firm rates</div></div>
        <div class="stat-box"><div class="stat-box-num">£100/mo</div><div class="stat-box-lbl">From — monthly retainer</div></div>
      </div>
      <div class="info-box" style="margin-top:20px">
        <h3>SRA Transparency</h3>
        <p>We comply with all SRA transparency rules on pricing. Full details of our charges are available on request.</p>
      </div>
    </div>
  </div>
</div></section>""")

# freedom-rights.html
build(f"{BASE}/freedom-rights.html",
  "Freedom Rights", "", "", "",
  page_hero(
    '<a href="index.html">Home</a> <span>→ Freedom Rights</span>',
    "<em>Freedom Rights</em>",
    "Employment law at the intersection of civil liberties, human rights, and individual freedom."
  ) + """
<section class="sec"><div class="sec-inner">
  <div class="two-col-3">
    <div>
      <div class="sec-lbl">Freedom Rights</div>
      <h2 class="sec-title">Where employment law meets <em>civil liberties.</em></h2>
      <div class="prose">
        <p>In addition to its mainstream employment law work, Jackson Osborne has developed a practice in areas broadly described as "Freedom Rights" — cases involving the interface between employment law and civil liberties, freedom of expression, freedom of thought, conscience and religion, and related human rights.</p>
        <p>This work arises increasingly in employment contexts — for example, employees dismissed or subjected to detriment for expressing views protected under freedom of speech or conscience, or for refusing to comply with requirements that conflict with genuinely held beliefs.</p>
        <h3>Areas of work</h3>
      </div>
      <ul class="svc-list">
        <li>Freedom of expression in the workplace</li>
        <li>Religion or belief discrimination claims</li>
        <li>Philosophical belief claims (including gender-critical beliefs)</li>
        <li>Medical autonomy and workplace requirements</li>
        <li>Civil liberties in employment contexts</li>
        <li>Cases with human rights dimensions</li>
      </ul>
    </div>
    <div>
      <div class="info-box">
        <h3>Contact Us</h3>
        <p>If you believe you have been treated unfairly because of a belief you hold or a right you have exercised, please contact us for a confidential discussion.</p>
        <a href="contact.html" class="btn-p">Get in Touch →</a>
      </div>
    </div>
  </div>
</div></section>""")

# contact.html
build(f"{BASE}/contact.html",
  "Contact Us", "", "", "",
  page_hero(
    '<a href="index.html">Home</a> <span>→ Contact</span>',
    "Get in <em>Touch</em>",
    "All enquiries are treated in strictest confidence. We will respond promptly."
  ) + """
<section class="sec"><div class="sec-inner">
  <div class="two-col">
    <div>
      <div class="sec-lbl">Contact Us</div>
      <h2 class="sec-title">Speak to a <em>specialist today.</em></h2>
      <div class="prose" style="margin-bottom:32px">
        <p>Whether you are an employer managing a complex situation or a senior professional facing an employment dispute — we are ready to help. All enquiries are treated in the strictest confidence.</p>
      </div>
      <div class="form-grid">
        <div class="form-group"><label>First Name</label><input type="text" placeholder="Your first name"></div>
        <div class="form-group"><label>Last Name</label><input type="text" placeholder="Your last name"></div>
        <div class="form-group"><label>Email Address</label><input type="email" placeholder="your@email.com"></div>
        <div class="form-group"><label>Phone Number</label><input type="tel" placeholder="+44 ..."></div>
        <div class="form-group">
          <label>I am enquiring as</label>
          <select><option>An Employee</option><option>An Employer</option><option>A Director</option><option>Other</option></select>
        </div>
        <div class="form-group"><label>Subject</label><input type="text" placeholder="Brief description of your matter"></div>
        <div class="form-group form-full">
          <label>Your Message</label>
          <textarea placeholder="Please describe your situation briefly. All information is treated in strict confidence."></textarea>
        </div>
        <div class="form-full">
          <button class="btn-blue" type="submit">Send Enquiry →</button>
          <p class="form-notice">By submitting this form you consent to us contacting you regarding your enquiry. We will not pass your details to third parties. Jackson Osborne is authorised and regulated by the Solicitors Regulation Authority.</p>
        </div>
      </div>
    </div>
    <div>
      <div class="info-box">
        <h3>Office</h3>
        <p>Jackson Osborne<br>Employment Lawyers<br>Cardiff, Wales</p>
        <br>
        <p><strong style="color:var(--gold-lt)">Email</strong><br>info@jacksonosborne.co.uk</p>
      </div>
      <div class="pull-quote" style="margin-top:24px">"Responsive, clear, no surprises except a result far better than I thought possible."<cite>Technology Director, Large Finance Company</cite></div>
    </div>
  </div>
</div></section>""")


# ── EMPLOYERS/ ───────────────────────────────────────────────────────────────
print("\nEmployers pages:")

build(f"{BASE}/employers/index.html",
  "For Employers", "../", "../", "../",
  page_hero(
    '<a href="../index.html">Home</a> <span>→ For Employers</span>',
    "For <em>Employers</em>",
    "Expert employment law advice and representation for businesses of all sizes — from SMEs to large corporates."
  ) + """
<section class="sec"><div class="sec-inner">
  <div class="two-col-3">
    <div>
      <div class="sec-lbl">Employer Services</div>
      <h2 class="sec-title">Protecting your business <em>at every stage.</em></h2>
      <div class="prose">
        <p>Jackson Osborne advises employers ranging from owner-managed businesses to large corporates. We deal with the full spectrum of employment law issues — from day-to-day HR queries to complex litigation before Employment Tribunals and the higher courts.</p>
        <p>Our partner and senior solicitor rates are 35–45% less than solicitors with equivalent experience in large commercial practices. We face such practices in disputes regularly — and come out winning, because we specialise entirely in employment law.</p>
      </div>
      <div class="card-grid">
        <div class="card"><h3>Tribunal &amp; Court</h3><p>Expert representation at Employment Tribunals and higher courts, from initial response through to full hearing.</p><a href="tribunal.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>Disciplinary &amp; Grievance</h3><p>Managing investigations, disciplinary processes and grievance hearings fairly, lawfully and effectively.</p><a href="disciplinary.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>Contracts &amp; Policies</h3><p>Drafting and updating employment contracts, handbooks and HR policies to protect your business.</p><a href="contracts.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>Redundancy</h3><p>Guiding you through redundancy processes that are fair, defensible and commercially effective.</p><a href="redundancy.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>Restrictive Covenants</h3><p>Drafting, enforcing and defending post-termination restrictions and confidentiality obligations.</p><a href="restrictive-covenants.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>TUPE &amp; Acquisitions</h3><p>Navigating business sales, acquisitions and outsourcing where TUPE regulations apply.</p><a href="tupe.html" class="card-link">Learn more →</a></div>
      </div>
    </div>
    <div>
      <div class="info-box">
        <h3>Monthly Retainer</h3>
        <p>Protect your business for as little as £1 per employee per week. Fixed cost. Senior advice. Full tribunal cover.</p>
        <a href="../monthly-retainer.html" class="btn-p">Find Out More →</a>
      </div>
      <div class="pull-quote">"Direct and to the point. Jackson Osborne have saved us many thousands of pounds."<cite>Robert Humphries, MD — B.A.S. International</cite></div>
    </div>
  </div>
</div></section>""")

def employer_page(filename, title, subtitle, breadcrumb_label, content):
    build(f"{BASE}/employers/{filename}",
      title, "../", "../", "../",
      page_hero(
        f'<a href="../index.html">Home</a> → <a href="index.html">For Employers</a> <span>→ {breadcrumb_label}</span>',
        title, subtitle
      ) + content)

employer_page("tribunal.html",
  "Tribunal &amp; Court <em>Representation</em>",
  "Expert, experienced representation at every level — from Employment Tribunal through to the Court of Appeal.",
  "Tribunal &amp; Court Representation",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>When a claim is issued against your business, how it is handled from the outset can make the difference between a successful outcome and a very expensive one. We handle every aspect of Employment Tribunal and court proceedings, from the initial response to full hearing.</p>
      <p>We are experienced advocates who appear regularly before Employment Tribunals and the Employment Appeal Tribunal. We face large commercial firms in disputes — and we win, because we specialise entirely in employment law and devote proper time and attention to each case.</p>
      <h3>What we handle</h3>
    </div>
    <ul class="svc-list">
      <li>Unfair dismissal claims</li>
      <li>Discrimination claims (all protected characteristics)</li>
      <li>Whistleblowing (protected disclosure) claims</li>
      <li>Breach of contract and wrongful dismissal</li>
      <li>Equal pay claims</li>
      <li>TUPE-related claims</li>
      <li>Injunctive proceedings in the High Court</li>
      <li>Appeals to the Employment Appeal Tribunal</li>
    </ul>
    <a href="../contact.html" class="btn-blue">Discuss Your Case →</a>
  </div>
  <div>
    <div class="info-box"><h3>Settlement</h3><p>Many disputes are best resolved by negotiated settlement. We achieve excellent results through skilled negotiation as well as full advocacy.</p><a href="settlement.html" class="btn-p">Learn More →</a></div>
    <div class="pull-quote">"We face large commercial practices in disputes — and win."<cite>Stephen Jackson, Principal</cite></div>
  </div>
</div></div></section>""")

employer_page("disciplinary.html",
  "Disciplinary, Grievance <em>&amp; Investigations</em>",
  "Managing difficult employment situations fairly, lawfully and decisively.",
  "Disciplinary &amp; Investigations",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>Poorly handled disciplinary and grievance processes are among the most common reasons employers face Tribunal claims. Getting the procedure right — and the substance right — requires expertise. We advise and support employers throughout, from initial investigation through to any appeal.</p>
      <h3>Workplace investigations</h3>
      <p>Where an independent investigation is needed — for example involving senior employees, allegations of discrimination or harassment, or complex financial misconduct — we can conduct or oversee the investigation to ensure it withstands scrutiny.</p>
    </div>
    <ul class="svc-list">
      <li>Advice on whether there are grounds for disciplinary action</li>
      <li>Drafting investigation and hearing procedures</li>
      <li>Conducting or overseeing investigations</li>
      <li>Advising on outcomes, including dismissal</li>
      <li>Managing appeals</li>
      <li>Grievance procedure advice and support</li>
    </ul>
  </div>
  <div><div class="info-box"><h3>Get Advice Early</h3><p>The earlier you take advice, the better the outcome. Contact us before taking action — not after.</p><a href="../contact.html" class="btn-p">Get in Touch →</a></div></div>
</div></div></section>""")

employer_page("contracts.html",
  "Contracts &amp; <em>Policies</em>",
  "Properly drafted documentation that protects your business and reflects how you actually operate.",
  "Contracts &amp; Policies",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>Employment contracts and HR policies are the foundation of your employment relationships. Outdated, poorly drafted or missing documents leave you exposed. We draft, review and update employment contracts, director service agreements, staff handbooks and stand-alone policies.</p>
      <h3>Directors' Service Agreements</h3>
      <p>Directors require carefully tailored service agreements covering duties, remuneration, bonus and incentive arrangements, post-termination restrictions, and termination provisions. We advise both companies and directors.</p>
      <h3>What we provide</h3>
    </div>
    <ul class="svc-list">
      <li>Employment contracts (all levels)</li>
      <li>Directors' service agreements</li>
      <li>Staff handbooks and HR policies</li>
      <li>Disciplinary and grievance procedures</li>
      <li>Redundancy and restructuring policies</li>
      <li>Data protection and confidentiality policies</li>
      <li>Social media policies</li>
      <li>Flexible working policies</li>
    </ul>
  </div>
  <div><div class="info-box"><h3>Documentation Audit</h3><p>Under the Monthly Retainer, we carry out a full review and update of your employment documentation as standard.</p><a href="../monthly-retainer.html" class="btn-p">Learn About Retainer →</a></div></div>
</div></div></section>""")

employer_page("directors.html",
  "Directors' Service <em>Agreements</em>",
  "Carefully drafted agreements that protect both the company and the director.",
  "Directors' Service Agreements",
  """<section class="sec"><div class="sec-inner"><div class="prose">
  <p>A director's service agreement is the most important employment document in most businesses. It governs duties, remuneration, bonus entitlement, long-term incentives, termination provisions, and post-termination restrictions. Both companies and directors instruct us to advise on and negotiate these agreements.</p>
  <p>We advise on the full range of director-level issues, including removal from office, shareholder disputes, board-level disputes, and the interaction between the service agreement and the company's articles of association and any shareholders' agreement.</p>
  <a href="../contact.html" class="btn-blue" style="margin-top:8px">Discuss Your Agreement →</a>
</div></div></section>""")

employer_page("redundancy.html",
  "Redundancy — <em>Getting It Right</em>",
  "Managing redundancy processes that are fair, legally sound, and commercially effective.",
  "Redundancy",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>Redundancy is one of the most legally complex and emotionally charged areas of employment law. A flawed process — however genuine the underlying commercial need — can result in unfair dismissal claims, discrimination claims, and significant liability.</p>
      <p>We advise employers on all aspects of redundancy, from initial planning through to completion, ensuring the process is fair, properly documented and defensible.</p>
      <h3>Collective redundancies</h3>
      <p>Where 20 or more redundancies are proposed within 90 days, strict collective consultation obligations apply, including informing and consulting employee representatives and notifying the Secretary of State. Failures here can lead to protective awards of up to 90 days' pay per employee.</p>
    </div>
    <ul class="svc-list">
      <li>Redundancy process design and planning</li>
      <li>Selection pool and criteria advice</li>
      <li>Individual consultation support</li>
      <li>Collective consultation (20+ redundancies)</li>
      <li>Redundancy payment calculations</li>
      <li>Settlement agreements on exit</li>
    </ul>
  </div>
  <div><div class="info-box"><h3>Plan Before You Act</h3><p>Taking advice before announcing any redundancy programme is essential to a successful outcome. Contact us at the earliest stage.</p><a href="../contact.html" class="btn-p">Get in Touch →</a></div></div>
</div></div></section>""")

employer_page("restrictive-covenants.html",
  "Restrictive Covenants <em>&amp; Confidentiality</em>",
  "Protecting your business interests when key employees depart.",
  "Restrictive Covenants",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>When a senior employee or director leaves, the risk of them joining a competitor, taking clients or soliciting colleagues can be significant. Well-drafted restrictions — and swift action to enforce them where necessary — can protect your business.</p>
      <h3>Enforcement</h3>
      <p>We act quickly when an employee or former employee is breaching their obligations. In appropriate cases we can obtain urgent injunctions from the High Court preventing ongoing breach. Speed is often critical.</p>
    </div>
    <ul class="svc-list">
      <li>Drafting enforceable post-termination restrictions</li>
      <li>Advising on enforceability of existing restrictions</li>
      <li>Sending cease and desist letters</li>
      <li>Applying for urgent injunctions</li>
      <li>Pursuing breach of confidentiality claims</li>
    </ul>
  </div>
  <div><div class="info-box"><h3>Act Quickly</h3><p>In restrictive covenant cases, delay can seriously damage your prospects of obtaining an injunction. Call us immediately.</p><a href="../contact.html" class="btn-p">Call Us Now →</a></div></div>
</div></div></section>""")

employer_page("discrimination.html",
  "Discrimination &amp; <em>Harassment</em>",
  "Defending employers against discrimination claims and building lawful, inclusive workplaces.",
  "Discrimination &amp; Harassment",
  """<section class="sec"><div class="sec-inner"><div class="prose">
  <p>Discrimination and harassment claims carry uncapped compensation and can result in very significant awards. They also carry reputational risk beyond the immediate financial exposure. We help employers both avoid claims by getting policies and practices right, and defend them robustly when they arise.</p>
  <p>We have successfully defended large employers against discrimination claims across all protected characteristics, and have experience of complex multi-party litigation involving allegations of institutional discrimination.</p>
  <a href="../contact.html" class="btn-blue" style="margin-top:8px">Discuss Your Situation →</a>
</div></div></section>""")

employer_page("tupe.html",
  "TUPE &amp; Business <em>Sales &amp; Acquisitions</em>",
  "Expert employment law advice on business transfers, outsourcings and service provision changes.",
  "TUPE &amp; Business Acquisitions",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>The Transfer of Undertakings (Protection of Employment) Regulations 2006 (TUPE) are complex and the consequences of getting them wrong can be severe. We advise buyers, sellers and incoming and outgoing service providers on all TUPE-related employment matters.</p>
      <h3>We advise on</h3>
    </div>
    <ul class="svc-list">
      <li>Whether TUPE applies to a proposed transaction</li>
      <li>Employee liability information obligations</li>
      <li>Appropriate information and consultation</li>
      <li>Post-transfer harmonisation of terms</li>
      <li>Dismissal and ETO defence</li>
      <li>Due diligence on employment matters in acquisitions</li>
    </ul>
  </div>
  <div><div class="info-box"><h3>Early Advice Essential</h3><p>TUPE obligations begin well before completion. Take advice at the earliest stage of any transaction.</p><a href="../contact.html" class="btn-p">Get in Touch →</a></div></div>
</div></div></section>""")

employer_page("settlement.html",
  "Settlement <em>Agreements</em>",
  "Achieving clean, cost-effective exits that protect your business.",
  "Settlement Agreements",
  """<section class="sec"><div class="sec-inner"><div class="prose">
  <p>Settlement agreements provide a legally binding mechanism to end employment and resolve potential claims. We draft and negotiate settlement agreements for employers, advising on appropriate compensation levels, confidentiality provisions, reference terms and post-termination restrictions.</p>
  <p>We often act quickly to resolve disputes before they reach the Tribunal, saving significant time and cost for all parties.</p>
  <a href="../contact.html" class="btn-blue" style="margin-top:8px">Discuss a Settlement →</a>
</div></div></section>""")


# ── EMPLOYEES/ ───────────────────────────────────────────────────────────────
print("\nEmployee pages:")

build(f"{BASE}/employees/index.html",
  "For Employees", "../", "../", "../",
  page_hero(
    '<a href="../index.html">Home</a> <span>→ For Employees</span>',
    "For <em>Employees</em>",
    "Protecting your rights and maximising your position — specialist advice for executives, senior managers and City professionals."
  ) + """
<section class="sec"><div class="sec-inner">
  <div class="two-col-3">
    <div>
      <div class="sec-lbl">Employee Services</div>
      <h2 class="sec-title">Your rights, <em>robustly defended.</em></h2>
      <div class="prose">
        <p>We act for employees at all levels — from those on modest salaries to senior executives and City professionals earning significant packages. We have achieved some of the highest compensation awards made by Employment Tribunals in Wales and the UK, including the third highest disability discrimination award in UK history.</p>
      </div>
      <div class="card-grid">
        <div class="card"><h3>Unfair Dismissal</h3><p>Whether dismissed outright or constructively forced out, we will assess your claim and fight for proper compensation.</p><a href="unfair-dismissal.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>Settlement Agreements</h3><p>We negotiate the best possible terms when your employment is ending, ensuring you are properly protected.</p><a href="settlement.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>Discrimination</h3><p>Claims of unfair treatment on grounds of race, sex, disability, age, religion or other protected characteristics.</p><a href="discrimination.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>Whistleblowing</h3><p>Protection for those who have made or wish to make protected disclosures about wrongdoing in the workplace.</p><a href="whistleblowing.html" class="card-link">Learn more →</a></div>
        <div class="card"><h3>Restrictive Covenants</h3><p>Advice on whether post-termination restrictions are enforceable and how to protect your future career.</p><a href="restrictive-covenants.html" class="card-link">Learn more →</a></div>
      </div>
    </div>
    <div>
      <div class="stat-row" style="grid-template-columns:1fr 1fr;margin-top:0">
        <div class="stat-box"><div class="stat-box-num">£559k</div><div class="stat-box-lbl">Record payout achieved</div></div>
        <div class="stat-box"><div class="stat-box-num">3rd</div><div class="stat-box-lbl">Highest disability award UK</div></div>
      </div>
      <div class="pull-quote">"Awesome to witness you at work. A result far better than I thought possible."<cite>Technology Director, Large Finance Company</cite></div>
      <div class="info-box">
        <h3>Free Initial Consultation</h3>
        <p>Contact us to discuss your situation confidentially. We will give you an honest assessment of your position and options.</p>
        <a href="../contact.html" class="btn-p">Get in Touch →</a>
      </div>
    </div>
  </div>
</div></section>""")

def employee_page(filename, title, subtitle, breadcrumb_label, content):
    build(f"{BASE}/employees/{filename}",
      title, "../", "../", "../",
      page_hero(
        f'<a href="../index.html">Home</a> → <a href="index.html">For Employees</a> <span>→ {breadcrumb_label}</span>',
        title, subtitle
      ) + content)

employee_page("unfair-dismissal.html",
  "Unfair &amp; Constructive <em>Dismissal</em>",
  "If you have been dismissed or felt forced to resign, you may have a strong claim for compensation.",
  "Unfair Dismissal",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>Unfair dismissal occurs when your employer terminates your employment without a fair reason or without following a fair procedure. Constructive dismissal occurs when your employer's conduct is so unreasonable that you are effectively forced to resign.</p>
      <p>To bring an unfair dismissal claim, you generally need two years' continuous service. However, some dismissals are automatically unfair from day one — including dismissals connected to whistleblowing, pregnancy, or asserting a statutory right.</p>
      <h3>Compensation</h3>
      <p>Compensation consists of a basic award and a compensatory award for actual financial loss, currently capped at £102,194 or one year's gross pay (whichever is lower). Some claims — such as whistleblowing — carry no cap at all.</p>
      <h3>Constructive Dismissal</h3>
      <p>This arises where your employer has committed a fundamental breach of your employment contract — for example by demoting you, removing responsibilities, failing to address bullying, or cutting your pay. We assess carefully whether circumstances amount to a breach and advise on timing and tactics.</p>
    </div>
    <div class="faq">
      <div class="faq-item">
        <button class="faq-q">How long do I have to bring a claim? <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
        <div class="faq-a"><div class="faq-a-inner">You must bring your Employment Tribunal claim within 3 months less one day from the effective date of termination. Acting promptly is essential.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">What is ACAS Early Conciliation? <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
        <div class="faq-a"><div class="faq-a-inner">Before issuing a Tribunal claim, you must notify ACAS and undergo Early Conciliation. This can extend your time limit. We can guide you through this process.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Can I still claim if I resigned? <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
        <div class="faq-a"><div class="faq-a-inner">Yes — if your employer's conduct forced you to resign, this may amount to constructive dismissal, which is treated as unfair dismissal in law.</div></div>
      </div>
    </div>
  </div>
  <div>
    <div class="info-box"><h3>Free Consultation</h3><p>Contact us to discuss your situation confidentially. We will give you an honest assessment of your position and prospects.</p><a href="../contact.html" class="btn-p">Get in Touch →</a></div>
    <div class="pull-quote">"A result far better than I thought possible."<cite>Technology Director, Large Finance Company</cite></div>
  </div>
</div></div></section>""")

employee_page("settlement.html",
  "Settlement <em>Agreements</em>",
  "Ensuring you receive the best possible terms when your employment is ending.",
  "Settlement Agreements",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>A settlement agreement is a legally binding contract between you and your employer, typically entered into when employment is ending. In exchange for agreeing not to bring Employment Tribunal claims, you receive a financial payment and other benefits.</p>
      <p>To be legally valid, you must receive independent legal advice on the agreement — which is where we come in. In most cases your employer will contribute towards your legal costs.</p>
      <h3>Negotiating the best deal</h3>
      <p>We don't just sign off on whatever your employer puts in front of you. We review the agreement carefully, advise whether the terms are fair, and where appropriate negotiate improvements — including increased compensation, extended notice payments, favourable references, and removal of restrictive covenants.</p>
      <h3>Senior executives</h3>
      <p>For senior employees and City professionals, settlement negotiations can involve complex issues around bonus entitlements, share schemes, LTIPs, pension rights, and garden leave. We have extensive experience advising on and negotiating these packages.</p>
    </div>
  </div>
  <div><div class="info-box"><h3>Acting Quickly Matters</h3><p>Time limits apply to any underlying claims you may have. Contact us as soon as you receive a settlement agreement.</p><a href="../contact.html" class="btn-p">Get Advice →</a></div></div>
</div></div></section>""")

employee_page("discrimination.html",
  "Discrimination &amp; <em>Harassment</em>",
  "Robust representation for those who have suffered unfair treatment at work based on a protected characteristic.",
  "Discrimination &amp; Harassment",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>The Equality Act 2010 protects employees from discrimination, harassment and victimisation on the basis of nine protected characteristics: age, disability, gender reassignment, marriage and civil partnership, pregnancy and maternity, race, religion or belief, sex, and sexual orientation.</p>
      <h3>Types of discrimination</h3>
      <p>Direct discrimination occurs when you are treated less favourably because of a protected characteristic. Indirect discrimination occurs when a seemingly neutral policy puts people with a protected characteristic at a particular disadvantage. Harassment is unwanted conduct related to a protected characteristic that violates your dignity or creates an intimidating or offensive environment.</p>
      <h3>No cap on compensation</h3>
      <p>Unlike unfair dismissal, there is no cap on compensation in discrimination claims. We have achieved some of the largest awards in Wales and the UK — including the third highest disability discrimination award in UK legal history.</p>
    </div>
  </div>
  <div>
    <div class="stat-row" style="grid-template-columns:1fr;margin-top:0">
      <div class="stat-box"><div class="stat-box-num">3rd</div><div class="stat-box-lbl">Highest disability discrimination award in UK history</div></div>
      <div class="stat-box"><div class="stat-box-num">No cap</div><div class="stat-box-lbl">On discrimination compensation awards</div></div>
    </div>
    <a href="../contact.html" class="btn-blue" style="margin-top:20px">Discuss Your Claim →</a>
  </div>
</div></div></section>""")

employee_page("whistleblowing.html",
  "<em>Whistleblowing</em> Protection",
  "Protecting those who speak out about wrongdoing in the workplace.",
  "Whistleblowing",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>Whistleblowing law protects workers who make "protected disclosures" — disclosures of information showing wrongdoing such as criminal offences, breaches of legal obligations, miscarriages of justice, or health and safety dangers.</p>
      <p>If you have been dismissed, subjected to a detriment, or treated badly because you made or were believed to have made a protected disclosure, you may have a strong claim. There is no qualifying period of service and no cap on compensation.</p>
      <h3>We advise on</h3>
    </div>
    <ul class="svc-list">
      <li>Whether your disclosure qualifies as a protected disclosure</li>
      <li>What to do if you are considering making a disclosure</li>
      <li>Claims for automatic unfair dismissal</li>
      <li>Claims for detriment short of dismissal</li>
      <li>Injunctions to prevent ongoing detriment</li>
    </ul>
  </div>
  <div><div class="info-box"><h3>Uncapped Compensation</h3><p>Whistleblowing claims carry no cap on compensation and no service requirement. Act promptly — time limits are strict.</p><a href="../contact.html" class="btn-p">Get Advice →</a></div></div>
</div></div></section>""")

employee_page("restrictive-covenants.html",
  "Restrictive <em>Covenants</em>",
  "Advice on post-termination restrictions and protecting your future career.",
  "Restrictive Covenants",
  """<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div>
    <div class="prose">
      <p>Many employment contracts contain post-termination restrictions preventing you from working for competitors, approaching clients, or soliciting colleagues. These clauses are only enforceable if they go no further than is reasonably necessary to protect a legitimate business interest.</p>
      <p>Many such clauses are too wide to be enforceable — but you need expert advice before breaching them, as getting it wrong can lead to injunctions and financial claims against you.</p>
      <h3>We advise on</h3>
    </div>
    <ul class="svc-list">
      <li>Whether your restrictions are likely to be enforceable</li>
      <li>Negotiating removal or reduction of restrictions on exit</li>
      <li>Responding to threats of injunction from a former employer</li>
      <li>Garden leave provisions</li>
      <li>Confidentiality obligations</li>
    </ul>
  </div>
  <div><div class="info-box"><h3>Act Before You Move</h3><p>Get advice before you join a competitor or approach former clients. We provide rapid, clear advice so you can move with confidence.</p><a href="../contact.html" class="btn-p">Get Advice →</a></div></div>
</div></div></section>""")


# ── NEWS/ ─────────────────────────────────────────────────────────────────────
print("\nNews pages:")

build(f"{BASE}/news/index.html",
  "News &amp; Know-how", "../", "../", "../",
  page_hero(
    '<a href="../index.html">Home</a> <span>→ News &amp; Know-how</span>',
    "News &amp; <em>Know-how</em>",
    "Case updates, legal developments, and practical guides from the firm."
  ) + """
<section class="sec"><div class="sec-inner">
  <div class="ng" style="margin-bottom:40px">
    <a href="royal-mint.html" class="nc ncf">
      <span class="n-date">July 2024</span><span class="n-tag">Case Win</span>
      <h3 class="n-title">Jackson Osborne win discrimination claim against The Royal Mint</h3>
      <p class="n-exc">A significant discrimination claim brought against The Royal Mint successfully concluded, adding to the firm's record of high-profile Employment Tribunal victories.</p>
      <span class="n-rd">Read more →</span>
    </a>
    <a href="court-protection.html" class="nc">
      <span class="n-date">July 2024</span><span class="n-tag">Court Win</span>
      <h3 class="n-title">Jackson Osborne Win in the Court of Protection</h3>
      <p class="n-exc">Successful outcome demonstrating the firm's capability in complex Court of Protection proceedings.</p>
      <span class="n-rd">Read more →</span>
    </a>
    <a href="bradley.html" class="nc">
      <span class="n-date">May 2024</span><span class="n-tag">Legal Update</span>
      <h3 class="n-title">Bradley v The Royal Mint — novel procedures</h3>
      <p class="n-exc">An insight into novel procedural aspects of this complex case and implications for future tribunal practice.</p>
      <span class="n-rd">Read more →</span>
    </a>
  </div>
  <div class="ng">
    <a href="record-award.html" class="nc ncf">
      <span class="n-date">March 2013</span><span class="n-tag">Record Award</span>
      <h3 class="n-title">Jackson Osborne wins over half a million pounds in discrimination claim</h3>
      <p class="n-exc">A landmark result — £558,868.66 for a client on a salary of just £17,000. The third highest disability discrimination award in UK history.</p>
      <span class="n-rd">Read more →</span>
    </a>
  </div>
</div></section>""")

def news_article(filename, title, date, tag, content):
    build(f"{BASE}/news/{filename}",
      title, "../", "../", "../",
      page_hero(
        f'<a href="../index.html">Home</a> → <a href="index.html">News</a> <span>→ {tag}</span>',
        title, date
      ) + f"""
<section class="sec"><div class="sec-inner"><div class="two-col-3">
  <div><div class="prose">{content}<a href="../contact.html" class="btn-blue" style="margin-top:16px">Discuss Your Case →</a></div></div>
  <div><div class="info-box"><h3>Similar Situation?</h3><p>Contact us for a confidential discussion about your employment matter.</p><a href="../contact.html" class="btn-p">Get in Touch →</a></div></div>
</div></div></section>""")

news_article("royal-mint.html",
  "Win Against <em>The Royal Mint</em>", "July 2024", "Case Win",
  "<p>Jackson Osborne successfully concluded a discrimination claim brought by our client against The Royal Mint, achieving a significant outcome before the Employment Tribunal. The case involved complex issues of discrimination law requiring detailed preparation and robust advocacy. This result adds to the firm's growing record of successful high-profile Employment Tribunal cases.</p><p>For confidentiality reasons, further details of the award and specific findings are not published here.</p>")

news_article("court-protection.html",
  "Win in the Court <em>of Protection</em>", "July 2024", "Court Win",
  "<p>Jackson Osborne secured a successful outcome in a Court of Protection matter, demonstrating the firm's expanding capability in complex multi-jurisdictional proceedings that intersect with employment and personal rights law.</p>")

news_article("bradley.html",
  "Bradley v The Royal Mint — <em>Novel Procedures</em>", "May 2024", "Legal Update",
  "<p>This case raised novel procedural questions before the Employment Tribunal, requiring careful analysis of the rules governing the conduct of proceedings and the interplay between different types of claim.</p><p>The procedural aspects of this matter will be of interest to employment law practitioners involved in complex multi-issue proceedings, illustrating the importance of having experienced solicitors familiar not just with the substantive law, but with the procedural rules that can determine the outcome of litigation.</p>")

news_article("record-award.html",
  "Record Award — <em>£558,868</em>", "March 2013", "Record Award",
  "<p>Jackson Osborne achieved an award of £558,868.66 for a client who had been suspended from work and was earning a salary of just £17,000. The award represented the third highest disability discrimination award in UK legal history at the time, and remains the highest Employment Tribunal award in Wales.</p><p>The case demonstrated that with the right specialist representation, employees on modest incomes can achieve life-changing results against well-resourced employers.</p>")

print("\n✅ All pages generated successfully.")
