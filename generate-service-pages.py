from pathlib import Path
from html import escape
import re
root=Path(__file__).resolve().parent
source=(root/'dist/index.html').read_text(encoding='utf-8')
start=source.index('<div class="services-grid">')+len('<div class="services-grid">')
end=source.index('</div><div class="services-cta">',start)
cards=re.findall(r'<article class="service-card">.*?</article>',source[start:end],re.S)
assert len(cards)==6, 'Expected six service cards on homepage'
homepage_cards = {re.search(r'<h3>(.*?)</h3>', card)[1]: card for card in cards}
pages=[
('checkup-exam','Dental Checkup & Exam','Looking for a dental checkup','in Leesburg?', 'Stay on top of your oral health with a thoughtful dental exam from the Russell Branch team.'),
('teeth-cleaning','Teeth Cleaning','Looking for a teeth cleaning','in Leesburg?', 'Give your smile a fresh start with professional dental care at Russell Branch Dental.'),
('lost-filling-crown','Lost Filling or Crown','Lost a filling or crown','in Leesburg?', 'Our team can assess your concern and talk you through the next steps for your smile.'),
('tooth-pain','Tooth Pain','Dealing with tooth pain','in Leesburg?', 'Let our team take a closer look and help you understand your options for care.'),
('emergency-dentist','Emergency Dentist','Need an emergency dentist','in Leesburg?', 'When a dental concern needs attention, contact our team to discuss what to do next.'),
('broken-cracked-tooth','Broken or Cracked Tooth','Have a broken or cracked tooth','in Leesburg?', 'Our dental team can evaluate your tooth and help you understand your treatment options.'),
('wisdom-teeth','Wisdom Teeth Removal','Looking for wisdom teeth care','in Leesburg?', 'Get a thoughtful assessment and a care plan tailored to your wisdom teeth.'),
('swelling-abscess','Dental Swelling or Abscess','Concerned about dental swelling','in Leesburg?', 'Contact our team about dental swelling or an abscess so we can discuss your next step.'),
('new-patient','New Patient Dentist','Looking for a new dentist','in Leesburg?', 'We welcome new patients and make it easy to take the first step toward your dental visit.'),
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


emergency_pages = {
    'lost-filling-crown', 'tooth-pain', 'emergency-dentist',
    'broken-cracked-tooth', 'swelling-abscess',
}
emergency_services = [
    ('Tooth pain', 'emergency-patient.webp', 'Tell us where it hurts and when it started so our team can arrange an evaluation.'),
    ('Broken or cracked tooth', 'emergency-dental.jpg', 'We can examine the damage and talk through options for repairing or treating the tooth.'),
    ('Wisdom tooth problem', 'wisdom-teeth.jpg', 'We can assess painful or irritated wisdom teeth and discuss whether oral surgery is appropriate.'),
    ('Swelling', 'dental-swelling.webp', 'Let our team know where you notice swelling so we can discuss the next step.'),
    ('Dental infection', 'root-canal.webp', 'We can examine the affected area and explain your treatment options.'),
    ('Knocked-out tooth', 'knocked-out-tooth.webp', 'Call us right away to discuss an urgent dental visit.'),
    ('Lost crown or filling', 'lost-dental-crown.webp', 'We can check the tooth and talk through options for restoring it.'),
]


def service_card(title, image, description):
    return (
        '<article class="service-card"><div class="service-art" aria-hidden="true">'
        f'<img src="assets/services/{image}" alt="" loading="lazy"></div>'
        f'<h3>{escape(title)}</h3><p>{escape(description)}</p></article>'
    )


# Keep campaign-specific service selections independent from the emergency form options.
related_services = {
    'checkup-exam': ('Regular checkup / cleaning', 'Dental exams', 'Cavity checks'),
    'teeth-cleaning': ('Professional teeth cleaning', 'Dental exams', 'Family dentistry'),
    'lost-filling-crown': ('Lost crown or filling', 'Broken or cracked tooth', 'Tooth pain'),
    'tooth-pain': ('Tooth pain', 'Dental infection', 'Swelling'),
    'broken-cracked-tooth': ('Broken or cracked tooth', 'Tooth pain', 'Lost crown or filling'),
    'wisdom-teeth': ('Wisdom teeth removal / oral surgery', 'Tooth extractions', 'Swelling'),
    'swelling-abscess': ('Swelling', 'Dental infection', 'Tooth pain'),
    'new-patient': ('Family dentistry', 'Regular checkup / cleaning', 'Dental emergencies'),
}
service_intros = {
    'checkup-exam': 'See what our team can check during a routine visit and how we can help spot concerns early.',
    'teeth-cleaning': 'Explore professional cleaning, exams, and ongoing care to help keep your teeth and gums healthy.',
    'lost-filling-crown': 'Explore care for a lost filling or crown and related concerns, such as damage or pain in the affected tooth.',
    'tooth-pain': 'Get help with a sore tooth and related concerns, including swelling or signs of infection.',
    'broken-cracked-tooth': 'Explore care for a damaged tooth and related concerns, such as pain or a loosened restoration.',
    'wisdom-teeth': 'Explore wisdom teeth evaluation, removal, and care for concerns such as swelling.',
    'swelling-abscess': 'Get help with dental swelling, possible infection, or pain in the affected area.',
}
emergency_cards = {item[0]: service_card(*item) for item in emergency_services}
service_cards = {**homepage_cards, **emergency_cards}
for item in [
    ('Dental exams', 'dental-exams.jpg', 'We examine your teeth and gums and explain any changes or concerns we find.'),
    ('Cavity checks', 'cavities.jpg', 'We look for signs of tooth decay and discuss what to do if we find a cavity.'),
    ('Professional teeth cleaning', 'tooth-cleaning.jpg', 'Our team removes plaque and tartar and shares tips for caring for your teeth between visits.'),
    ('Tooth extractions', 'extractions.jpg', 'If a wisdom tooth needs to be removed, we’ll explain the procedure and what to expect during recovery.'),
]:
    service_cards[item[0]] = service_card(*item)


def tailor_emergency_page(page):
    page = page.replace('<section class="team" id="dentists">', '<section class="team emergency-team" id="dentists">')
    page = page.replace('Get to know the team behind your smile.', 'Meet the doctors who provide emergency dental care at Russell Branch Dental.')
    for name in ('Dr. Afsaneh Rangiani', 'Dr. Gia Duong'):
        page = re.sub(r'<article class="team-card">(?:(?!</article>).)*?<h3>' + re.escape(name) + r'</h3>.*?</article>', '', page, count=1, flags=re.S)
    page = page.replace('He is a national implant surgery educator.</p>',
        'He is a national implant surgery educator. For emergency visits, he evaluates the problem and explains the treatment options and next steps.</p>')
    page = page.replace('including wisdom teeth extractions under deep sedation.</p>',
        'including wisdom teeth extractions under deep sedation. He evaluates urgent concerns that may need oral surgery and discusses the available options.</p>')
    page = page.replace('<li><span class="check">✓</span>Family, cosmetic &amp; emergency dentistry</li>', '')
    page = page.replace('Come smile with us.', "Let’s take care of your dental emergency.")
    page = page.replace('Tell us a little about yourself and take the first step toward your visit.',
        'Choose the reason for your visit, then continue to online booking.')
    options = '<option value="">Select a reason for your visit</option>'
    options += ''.join(f'<option>{escape(reason)}</option>' for reason in [item[0] for item in emergency_services] + ['Something else'])
    page, count = re.subn(r'(<select id="(?:modal-)?visit"[^>]*>).*?(</select>)',
        lambda match: match[1] + options + match[2], page, flags=re.S)
    assert count == 2
    page = page.replace('CARE FOR YOUR WHOLE SMILE', 'EMERGENCY DENTAL CARE').replace('Care for your whole smile', 'Emergency dental care')
    page = page.replace('From routine visits to unexpected concerns, find thoughtful dental care for every stage of your smile.',
        'From sudden tooth pain to a lost crown, see the urgent dental concerns we can help with.')
    return page.replace('</style>', '\n@media(min-width: 561px){.emergency-team .team-grid{grid-template-columns:repeat(2,minmax(0,1fr));max-width:820px;margin-inline:auto}}</style>', 1)


hero='Looking for a dentist <span class="accent">in Leesburg?</span>'
intro='Meet your Leesburg dentist for thoughtful, comprehensive care and a smile that feels like you.'
for slug,title,line1,line2,description in pages:
 page=source.replace('<title>Leesburg Dentist | Russell Branch Dental</title>',f'<title>{escape(title)} in Leesburg, VA | Russell Branch Dental</title>')
 page=page.replace('content="Comfortable, comprehensive dental care for your family in Leesburg, Virginia."',f'content="{escape(description, quote=True)}"')
 page=page.replace(hero,escape(line1)+' <span class="accent">'+escape(line2)+'</span>')
 page=page.replace(intro,escape(description))
 page=page.replace('Our services, <span class="accent">centered on you.</span>', escape(service_titles[slug])+', <span class="accent">centered on you.</span>')
 faq_start=page.index('<div class="faq-list">')+len('<div class="faq-list">')
 faq_end=page.index('</div></div></section><section class="office"', faq_start)
 faq=''.join('<details><summary>'+escape(q)+'</summary><p>'+escape(answer).replace('(703) 771-2670', '<span data-practice-phone>(703) 771-2670</span>')+'</p></details>' for q,answer in questions[slug]+general_questions)
 page=page[:faq_start]+faq+page[faq_end:]

 a=page.index('<div class="services-grid">')+len('<div class="services-grid">');b=page.index('</div><div class="services-cta">',a)
 selected_cards = (list(emergency_cards.values()) if slug == 'emergency-dentist'
                   else [service_cards[name] for name in related_services[slug]])
 page=page[:a]+''.join(selected_cards)+page[b:]
 if slug in emergency_pages:
  page = tailor_emergency_page(page)
 if slug in service_intros:
  generic_intro = ('From sudden tooth pain to a lost crown, see the urgent dental concerns we can help with.'
                   if slug in emergency_pages else
                   'From routine visits to unexpected concerns, find thoughtful dental care for every stage of your smile.')
  page = page.replace(generic_intro, escape(service_intros[slug]), 1)
 page=page.replace('src="assets/', 'src="/assets/')
 out=root/'dist'/slug/'index.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(page,encoding='utf-8')
 print(f'{slug}: '+', '.join(re.search(r'<h3>(.*?)</h3>',card).group(1) for card in selected_cards))
