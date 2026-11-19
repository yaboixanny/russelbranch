from pathlib import Path
from html import escape
import re
root=Path(__file__).resolve().parent
source=(root/'dist/index.html').read_text(encoding='utf-8')
start=source.index('<div class="services-grid">')+len('<div class="services-grid">')
end=source.index('</div><div class="services-cta">',start)
cards=re.findall(r'<article class="service-card">.*?</article>',source[start:end],re.S)
assert len(cards)==9, 'Expected nine service cards on homepage'
pages=[
('checkup-exam','Dental Checkup & Exam','Looking for a dental checkup','in Leesburg?', 'Stay on top of your oral health with a thoughtful dental exam from the Russell Branch team.', [1,4,8]),
('teeth-cleaning','Teeth Cleaning','Looking for a teeth cleaning','in Leesburg?', 'Give your smile a fresh start with professional dental care at Russell Branch Dental.', [8,1,4]),
('lost-filling-crown','Lost Filling or Crown','Lost a filling or crown','in Leesburg?', 'Our team can assess your concern and talk you through the next steps for your smile.', [7,4,5]),
('tooth-pain','Tooth Pain','Dealing with tooth pain','in Leesburg?', 'Let our team take a closer look and help you understand your options for care.', [7,4,5]),
('emergency-dentist','Emergency Dentist','Need an emergency dentist','in Leesburg?', 'When a dental concern needs attention, contact our team to discuss what to do next.', [7,6,4]),
('broken-cracked-tooth','Broken or Cracked Tooth','Have a broken or cracked tooth','in Leesburg?', 'Our dental team can evaluate your tooth and help you understand your treatment options.', [7,4,6]),
('wisdom-teeth','Wisdom Teeth Removal','Looking for wisdom teeth care','in Leesburg?', 'Get a thoughtful assessment and a care plan tailored to your wisdom teeth.', [2,6,4]),
('swelling-abscess','Dental Swelling or Abscess','Concerned about dental swelling','in Leesburg?', 'Contact our team about dental swelling or an abscess so we can discuss your next step.', [7,4,6]),
('new-patient','New Patient Dentist','Looking for a new dentist','in Leesburg?', 'We welcome new patients and make it easy to take the first step toward your dental visit.', [0,4,8]),
]
hero='Looking for a dentist <span class="accent">in Leesburg?</span>'
intro='Meet your Leesburg dentist for thoughtful, comprehensive care and a smile that feels like you.'
for slug,title,line1,line2,description,selected in pages:
 page=source.replace('<title>Leesburg Dentist | Russell Branch Dental</title>',f'<title>{escape(title)} in Leesburg, VA | Russell Branch Dental</title>')
 page=page.replace('content="Comfortable, comprehensive dental care for your family in Leesburg, Virginia."',f'content="{escape(description, quote=True)}"')
 page=page.replace(hero,escape(line1)+' <span class="accent">'+escape(line2)+'</span>')
 page=page.replace(intro,escape(description))
 a=page.index('<div class="services-grid">')+len('<div class="services-grid">');b=page.index('</div><div class="services-cta">',a)
 page=page[:a]+''.join(cards[i] for i in selected)+page[b:]
 page=page.replace('src="assets/', 'src="/assets/')
 out=root/'dist'/slug/'index.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(page,encoding='utf-8')
 print(f'{slug}: '+', '.join(re.search(r'<h3>(.*?)</h3>',cards[i]).group(1) for i in selected))
