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
('new-patient','New Patient Dentist','Looking for a new dentist','in Leesburg?', 'We welcome new patients and make it easy to take the first step toward your dental visit.', [0,8,7]),
]

service_titles={
 'checkup-exam':'Our dental checkup and exam services',
 'teeth-cleaning':'Our teeth cleaning services',
 'lost-filling-crown':'Our lost filling and crown services',
 'tooth-pain':'Our tooth pain services',
 'emergency-dentist':'Our dental emergency services',
 'broken-cracked-tooth':'Our broken and cracked tooth services',
 'wisdom-teeth':'Our wisdom teeth services',
 'swelling-abscess':'Our dental swelling and abscess services',
 'new-patient':'Our new patient dental services',
}
questions={
 'checkup-exam':[
  ('What happens at a dental checkup?', 'Your dental team will review your oral health, examine your teeth and gums, and discuss any concerns or recommendations with you.'),
  ('How often should I have a dental exam?', 'Your dentist can recommend a schedule based on your oral health and individual needs.'),
  ('Can I discuss a dental concern during my checkup?', 'Yes. Let your dental team know about any changes, discomfort, or questions you have.'),
  ('Is a cleaning part of my visit?', 'Your care depends on your needs and appointment. Ask our team what is planned when you schedule.')],
 'teeth-cleaning':[
  ('What happens during a professional teeth cleaning?', 'A dental professional cleans your teeth and can discuss your oral hygiene routine and any concerns you have.'),
  ('How often should I have my teeth cleaned?', 'Your dental team can suggest a cleaning schedule based on your oral health.'),
  ('Can I schedule an exam with my cleaning?', 'Contact our team to discuss the right appointment for your needs, including an exam and cleaning.'),
  ('What if I have sensitive teeth?', 'Let your dental team know before your visit so they can discuss your concerns and approach to care.')],
 'lost-filling-crown':[
  ('What should I do if I lose a filling or crown?', 'Call our office to explain what happened. Our team can help you arrange an evaluation and discuss next steps.'),
  ('Can a lost crown be put back on?', 'That depends on the condition of the crown and tooth. The dentist will assess them and discuss your options.'),
  ('What if my tooth hurts after a filling or crown comes out?', 'Call us and tell the team about your symptoms so they can help you determine the next step.'),
  ('Will I need a new filling or crown?', 'Your dentist will examine the tooth and recommend treatment based on its condition.')],
 'tooth-pain':[
  ('What should I do if I have a toothache?', 'Call our office and describe your symptoms. Our team can help you arrange an evaluation.'),
  ('What can cause tooth pain?', 'Tooth pain can have several causes. An examination helps the dentist assess your concern and discuss possible treatment.'),
  ('Can you help with urgent tooth pain?', 'Our practice offers emergency dental care. Call us to discuss your symptoms and appointment options.'),
  ('What happens during a tooth pain appointment?', 'Your dentist will assess the area, discuss your symptoms, and explain appropriate next steps.')],
 'emergency-dentist':[
  ('What dental emergencies can you help with?', 'Our team can assess urgent concerns such as tooth pain, a broken tooth, or a lost filling or crown. Call us to discuss your situation.'),
  ('How do I request an emergency dental appointment?', 'Call our team at (703) 771-2670 and describe your concern so we can discuss appointment options.'),
  ('What happens at an emergency dental visit?', 'Your dentist will assess your concern and discuss the appropriate next steps and treatment options.'),
  ('Can new patients contact you for an urgent concern?', 'Yes. Call our office to tell us what is happening and ask about an appointment.')],
 'broken-cracked-tooth':[
  ('What should I do if I break or crack a tooth?', 'Call our office to describe what happened. Our team can help you arrange an evaluation.'),
  ('Can a cracked tooth be repaired?', 'Treatment depends on the location and extent of the damage. Your dentist will examine the tooth and discuss your options.'),
  ('What if my broken tooth does not hurt?', 'A dental examination can help determine the condition of the tooth, even when there is no pain.'),
  ('Can you see me for an urgent broken tooth?', 'Our practice offers emergency dental care. Call us to discuss your concern and appointment options.')],
 'wisdom-teeth':[
  ('How do I know if my wisdom teeth need to be removed?', 'Your dentist can evaluate your wisdom teeth and discuss whether removal or another approach is appropriate for you.'),
  ('Does everyone need their wisdom teeth removed?', 'Not necessarily. The recommendation depends on your individual situation and dental evaluation.'),
  ('What happens during a wisdom teeth consultation?', 'Your dentist will assess your wisdom teeth, discuss your concerns, and explain possible next steps.'),
  ('What if my wisdom teeth are causing discomfort?', 'Call our office and tell the team about your symptoms so we can discuss an evaluation.')],
 'swelling-abscess':[
  ('What should I do about dental swelling or a possible abscess?', 'Call our office and describe your symptoms. Our team can help you arrange an evaluation and discuss next steps.'),
  ('Can you help with an urgent dental concern?', 'Our practice offers emergency dental care. Call us to discuss your symptoms and appointment options.'),
  ('What happens when I come in for swelling?', 'Your dentist will assess the area, discuss your symptoms, and explain appropriate next steps.'),
  ('Will I need treatment for an abscess?', 'Treatment depends on the diagnosis. Your dentist will explain your options after an evaluation.')],
 'new-patient':[
  ('Are you accepting new patients?', 'Yes. Russell Branch Dental welcomes new patients of all ages. Call or use the online booking link to get started.'),
  ('What can I expect at my first visit?', 'Your dental team will discuss your concerns, review your oral health, and explain any recommended next steps.'),
  ('Can I schedule a cleaning as a new patient?', 'Contact our team to discuss the right first appointment for your needs, including an exam and cleaning.'),
  ('Do you see patients of all ages?', 'Yes. Our practice welcomes new patients of all ages.')],
}
general_questions=[
 ('Where is your Leesburg office?', 'We are located at 135 Robinson Mill Plaza SE, Unit 108, Leesburg, VA 20175.'),
 ('Do you offer financing?', 'The practice offers financing options through CareCredit and Sunbit. Contact our team for details and eligibility.'),
]

hero='Looking for a dentist <span class="accent">in Leesburg?</span>'
intro='Meet your Leesburg dentist for thoughtful, comprehensive care and a smile that feels like you.'
for slug,title,line1,line2,description,selected in pages:
 page=source.replace('<title>Leesburg Dentist | Russell Branch Dental</title>',f'<title>{escape(title)} in Leesburg, VA | Russell Branch Dental</title>')
 page=page.replace('content="Comfortable, comprehensive dental care for your family in Leesburg, Virginia."',f'content="{escape(description, quote=True)}"')
 page=page.replace(hero,escape(line1)+' <span class="accent">'+escape(line2)+'</span>')
 page=page.replace(intro,escape(description))
 page=page.replace('Our services, <span class="accent">centered on you.</span>', escape(service_titles[slug])+', <span class="accent">centered on you.</span>')
 faq_start=page.index('<div class="faq-list">')+len('<div class="faq-list">')
 faq_end=page.index('</div></div></section><section class="office"', faq_start)
 faq=''.join('<details><summary>'+escape(q)+'</summary><p>'+escape(answer)+'</p></details>' for q,answer in questions[slug]+general_questions)
 page=page[:faq_start]+faq+page[faq_end:]

 a=page.index('<div class="services-grid">')+len('<div class="services-grid">');b=page.index('</div><div class="services-cta">',a)
 selected_cards=[cards[i] for i in selected]
 if slug=='new-patient':
  selected_cards[0]=selected_cards[0].replace('<h3>Family dentistry</h3>', '<h3>Family dentistry &amp; dental exams</h3>').replace("Care for every stage of your family&#x27;s smile.", "Family dental care and exams for every stage of your smile.").replace('Preventive care and treatment planning', 'Dental exams and preventive care')
 page=page[:a]+''.join(selected_cards)+page[b:]
 page=page.replace('src="assets/', 'src="/assets/')
 out=root/'dist'/slug/'index.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(page,encoding='utf-8')
 print(f'{slug}: '+', '.join(re.search(r'<h3>(.*?)</h3>',cards[i]).group(1) for i in selected))
