from bs4 import BeautifulSoup
def assemble_segments(text_fragments): 
    print(text_fragments)
    # Step 1: Skip any fragment of size less than 8 
    filtered_fragments = [frag for frag in text_fragments if len(frag) >= 8] 
    segments = [] 
    current_segment = "" 
    
    # Step 2: Keep assembling a segment from the text fragments until its size is > 128 but not more than 256 
    for fragment in filtered_fragments: 
        if len(current_segment + fragment) <= 256: 
            current_segment += fragment 
            if len(current_segment) >= 128: 
                segments.append(current_segment) 
                current_segment = "" 
        else: 
            # Add as many full 128-length segments as possible 
            while len(current_segment) + 128 <= 256: 
                segments.append(current_segment[:128]) 
                current_segment = current_segment[128:] 
            # # If there's any remaining text, start a new segment with it 
            
            #Here there was one logical error - it should apend the remaining test to the segments and reset the current segment to and empty string 
            segments.append(current_segment) 
            current_segment = fragment 
    
    # Step 3: If the initial text fragment is too large, split it into chunks of 128 
    if len(current_segment) > 0: 
        for i in range(0, len(current_segment), 128): 
            segments.append(current_segment[i:i+128]) 
        current_segment = "" 
    
    return segments


# Example usage
html = "<html><body><p>Here is some text.</p><p>Here is some more text.</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
text_fragments = [tag.get_text() for tag in soup.find_all(text=True)]
segments = assemble_segments(text_fragments)

