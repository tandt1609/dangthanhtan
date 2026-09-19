#!/usr/bin/env perl
use strict;
use warnings;
use utf8;
use open ':std', ':encoding(UTF-8)';

my $source_file = '../file for wed/luoc-su-the-gioi.html';
my $index_file  = 'index.html';

print "Reading $source_file...\n";
open my $sf, '<:encoding(UTF-8)', $source_file or die "Cannot open $source_file: $!";
my $source_html = do { local $/; <$sf> };
close $sf;

# 1. Extract <style>
my ($style_content) = $source_html =~ m{<style>(.*?)</style>}s;
die "No <style> found in source" unless defined $style_content;

# Scope CSS
$style_content =~ s{:root\b}{&}g;
$style_content =~ s{\bbody\s*\{}{&.thegioi-body \{}g;
$style_content =~ s{\bhtml\s*\{}{&.thegioi-html \{}g;
# Make navigation inside panel sticky instead of fixed to prevent overlapping site header
$style_content =~ s{position:\s*fixed;\s*top:\s*0;}{position: sticky; top: 0;}g;
# Ensure sections are fully visible in case IntersectionObserver has delay
$style_content =~ s/\.era-section\s*\{\s*opacity:\s*0;\s*transform:\s*translateY\(24px\);/\.era-section { opacity: 1; transform: none; \}/g;

my $scoped_style = <<"CSS";
<style>
#article-thegioi-panel {
$style_content
}
</style>
CSS

# 2. Extract <body>
my ($body_content) = $source_html =~ m{<body>(.*?)</body>}s;
die "No <body> found in source" unless defined $body_content;

my $panel_html = <<"HTML";
<div id="article-thegioi-panel" class="sukien-article-panel thegioi-body">
$scoped_style
    <div style="padding: 14px 20px; background: #ede5d0; border-bottom: 1px solid #d4a843;">
        <button class="back-btn" onclick="openThuVienArticle('')" style="background: #f7f2e8; border: 1px solid #b8860b; color: #1a1208; padding: 7px 16px; cursor: pointer; font-family: 'Space Mono', monospace; font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em; border-radius: 4px;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại Thư viện
        </button>
    </div>
$body_content
    <div style="padding: 24px; text-align: center; background: #ede5d0; border-top: 1px solid #d4a843;">
        <button class="back-btn" onclick="openThuVienArticle('')" style="background: #f7f2e8; border: 1px solid #b8860b; color: #1a1208; padding: 8px 20px; cursor: pointer; font-family: 'Space Mono', monospace; font-size: 0.9rem; font-weight: 700; letter-spacing: 0.05em; border-radius: 4px;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại Thư viện
        </button>
    </div>
</div>
HTML

# 3. Read index.html
print "Reading $index_file...\n";
open my $inf, '<:encoding(UTF-8)', $index_file or die "Cannot open $index_file: $!";
my $index_html = do { local $/; <$inf> };
close $inf;

# A. Add Space Mono font if not present
my $font_tag = '<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">';
if ($index_html !~ /family=Space\+Mono/) {
    $index_html =~ s{(<link href="https://fonts\.googleapis\.com/css2\?family=Bricolage\+Grotesque:[^"]+" rel="stylesheet">)}{$1\n    $font_tag};
    print "Added Space Mono Google font\n";
}

# B. Insert card into Trang Chu (Home) news-list
my $home_card = <<"HCARD";
                        <!-- Post: Luoc Su The Gioi (Thu Vien) -->
                        <a href="/thu-vien/luoc-su-the-gioi" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-earth-americas"></i> Lịch sử &amp; Xã hội</span>
                                <span class="news-time">19/09/2026</span>
                            </div>
                            <h3 class="news-heading">Lược Sử Thế Giới &amp; Xã Hội Loài Người — Từ Khai Thiên Lập Địa Đến Kỷ Nguyên AI</h3>
                            <p class="news-excerpt">13,8 tỷ năm vũ trụ, 300.000 năm loài người và 10.000 năm văn minh. Toàn cảnh hành trình tiến hóa, trỗi dậy và sụp đổ của các đế chế cùng những bài học muôn đời.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc bài viết</span>
                            </div>
                        </a>
HCARD

if ($index_html !~ /id="panel-trang-chu".*?href="\/thu-vien\/luoc-su-the-gioi"/s) {
    # Insert at top of news-list in panel-trang-chu
    $index_html =~ s{(<div id="panel-trang-chu" class="tab-panel active">\s*<h2 class="section-title"><i class="fa-solid fa-fire-flame-curved"></i> Bài viết mới</h2>\s*<div class="news-list">)}{$1\n$home_card}s;
    print "Added card to Trang Chu (Home)\n";
} else {
    print "Card already exists in Trang Chu\n";
}

# C. Insert card into Thu Vien news-list
my $tv_card = <<"TVCARD";
                        <!-- Post: Luoc Su The Gioi (Thu Vien) -->
                        <a href="/thu-vien/luoc-su-the-gioi" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-earth-americas"></i> Lịch sử &amp; Xã hội</span>
                                <span class="news-time">Tháng 9, 2026</span>
                            </div>
                            <h3 class="news-heading">Lược Sử Thế Giới &amp; Xã Hội Loài Người — Từ Khai Thiên Lập Địa Đến Kỷ Nguyên AI</h3>
                            <p class="news-excerpt">13,8 tỷ năm vũ trụ, 300.000 năm loài người và 10.000 năm văn minh. Toàn cảnh hành trình tiến hóa, trỗi dậy và sụp đổ của các đế chế cùng những bài học muôn đời.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc bài viết</span>
                            </div>
                        </a>
TVCARD

if ($index_html !~ /id="panel-thu-vien".*?href="\/thu-vien\/luoc-su-the-gioi"/s) {
    my $tv_target = '<!-- Post: Luoc Su Con Duong To Lua (Thu Vien) -->';
    if ($index_html =~ /\Q$tv_target\E/) {
        $index_html =~ s{\Q$tv_target\E}{$tv_card\n$tv_target};
        print "Added card to Thu Vien\n";
    } else {
        # Fallback to news-list in panel-thu-vien
        $index_html =~ s{(<div id="panel-thu-vien"[^>]*>.*?<div class="news-list">)}{$1\n$tv_card}s;
        print "Added card to Thu Vien (fallback)\n";
    }
} else {
    print "Card already exists in Thu Vien\n";
}

# D. Insert article panel
if ($index_html !~ /id="article-thegioi-panel"/) {
    my $panel_target = qr{(\s*</div>\s*</div>\s*<!-- PANEL 7: GAME -->)};
    if ($index_html =~ $panel_target) {
        $index_html =~ s{$panel_target}{\n$panel_html\n$1};
        print "Added article-thegioi-panel\n";
    } else {
        # Alternate match
        my $panel_target2 = '<!-- PANEL 7: GAME -->';
        if ($index_html =~ /\Q$panel_target2\E/) {
            # Insert before the two closing divs right before PANEL 7: GAME
            $index_html =~ s{(</div>\s*</div>\s*<!-- PANEL 7: GAME -->)}{$panel_html\n                $1};
            print "Added article-thegioi-panel (alternate)\n";
        } else {
            die "Could not find panel target for PANEL 7: GAME\n";
        }
    }
} else {
    print "Panel already exists in index.html\n";
}

# Write index.html
open my $outf, '>:encoding(UTF-8)', $index_file or die "Cannot write $index_file: $!";
print $outf $index_html;
close $outf;
print "Successfully updated $index_file!\n";
